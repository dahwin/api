

import cv2
import os
import time
import threading
time.sleep(1)

url =  "http://127.0.0.1:3000/video_feed"

# Initialize VideoCapture object
cap = cv2.VideoCapture(url)

# Get the default frame size
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 3.6, (frame_width, frame_height))

# Function to continuously read frames and write them to the output video
def read_frames():
    frame_count = 0
    start_time = time.time()
    while frame_count < 100:
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            out.write(frame)
        else:
            print("Error reading frame")
            break
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken to get 100 frames:", elapsed_time, "seconds")

# Start reading frames in a separate thread
frame_thread = threading.Thread(target=read_frames)
frame_thread.start()

# Wait for the frame thread to finish
frame_thread.join()

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
