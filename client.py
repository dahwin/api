#perfect

import cv2
import time
import threading
from PIL import Image
import asyncio
import nest_asyncio

nest_asyncio.apply()
time.sleep(1)

# url =  "http://localhost:3000/video_feed"
url =  "http://127.0.0.1:8000/video_feed"
# url =  "https://video.queendahyun.com/video_feed"
# url =  "https://name.queendahyun.com/video_feed"
# Initialize VideoCapture object
cap = cv2.VideoCapture(url)

# Get the default frame size
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output0.avi', fourcc, 3.8, (frame_width, frame_height))

async def read_frames_async():
    start_time = time.time()
    frame_count = 0

    all_count = 0
    
    while frame_count < 100:
        ret, frame = cap.read()
        out.write(frame)


        frame_count += 1
        all_count +=1

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken to get frames:", elapsed_time, "seconds")
    print("Frame count:", frame_count)
    


# Start reading frames asynchronously
asyncio.run(read_frames_async())

# Release everything when done
cap.release()

