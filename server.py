
from fastapi import FastAPI
from starlette.responses import StreamingResponse
import cv2
import time
import uvicorn
import numpy as np
import datetime
import asyncio
from queue import Queue
import nest_asyncio
import threading
nest_asyncio.apply()
app = FastAPI()



global latest_frame, frame_changed, delay, l, num_frames

async def generate_frames():

    global latest_frame, frame_changed, delay, l, num_frames
    # Shared variable to store the latest frame
    latest_frame = None
    frame_changed = False
    # Variable for frame interval (in seconds) to achieve desired FPS
    frame_interval = 1 / 4
    start_time = time.time()
    
    url = "http://localhost:3000/video_feed"  # Update the URL if needed
    cap = cv2.VideoCapture(url)
    l = None
    num_frames = 0
    
    while True:
        # print(f'total {num_frames}')
        # Record start time of processing a frame
        frame_start_time = time.time()
        ret, frame = cap.read()
        l=num_frames
        

        if True:
            # Convert the frame to JPEG format for streaming
            _, buffer = cv2.imencode('.jpg', frame)

            num_frames += 1


            latest_frame = buffer.tobytes()  # Update the latest frame

        print(l)

        

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # If one second has elapsed, calculate and print FPS
        if elapsed_time >= 1:
            fps = num_frames / elapsed_time
            # print("FPS:", fps)

        frame_time = time.time() - frame_start_time
        # Calculate the delay required to achieve desired FPS
        delay = frame_interval - frame_time

        

        try:
            # Introduce the delay
            await asyncio.sleep(delay)
            l=num_frames
        except asyncio.CancelledError:
            break
@app.get("/video_feed")
async def video_feed():
    async def stream_frame():
        global latest_frame
        lc =[0,]

        while True:
            # all_frames +=1
            # if frame_changed==True:
            #     num_frames += 1
            ll = lc[-1]
            if l==ll:
                lc.append(l)
            # print(f'num frames {num_frames}')
            
            # print(f"l {l}")
            if num_frames > l and l!=ll:  # Check if there's a latest frame available
                    lc.append(l)
                    yield (
                        b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + latest_frame + b'\r\n'
                    )
            else:
                # print(delay)
                await asyncio.sleep(0.01)  # If no latest frame available, wait for a short time
        # print(f'total {num_frames}')


    return StreamingResponse(stream_frame(), media_type="multipart/x-mixed-replace; boundary=frame")

async def main():
    # Start generating frames asynchronously
    asyncio.create_task(generate_frames())

import multiprocessing



def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)
