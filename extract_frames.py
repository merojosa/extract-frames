import os
import shutil
import time
import pandas as pd
from pytube import YouTube
import cv2


def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=output_path, filename=f"{yt.video_id}.mp4")
    return os.path.join(output_path, f"{yt.video_id}.mp4")


def extract_frames(video_path, output_path, frame_rate):
    # Extract the file name from the video path
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) of the video
    fps = video.get(cv2.CAP_PROP_FPS)

    # Calculate the frame interval based on the desired frame rate
    frame_interval = round(fps / frame_rate)

    # Initialize variables
    frame_count = 0
    success = True

    while success:
        # Read a frame from the video
        success, frame = video.read()

        # Check if the current frame index is divisible by the frame interval
        if frame_count % frame_interval == 0:
            # Check if the frame is valid
            if frame is not None:
                # Construct the image file name using video name and count
                image_name = f"{video_name}_{frame_count}.png"
                image_path = os.path.join(output_path, image_name)

                # Resize the frame to 1280x720
                frame = cv2.resize(frame, (1280, 720))

                # Save the extracted frame as an image
                cv2.imwrite(image_path, frame)

        # Increment the frame count
        frame_count += 1

    # Release the video file
    video.release()


# Directory to save YT videos
videos_path = "videos"
shutil.rmtree(
    videos_path,
)
os.makedirs(videos_path, exist_ok=True)

# Directory to save the images
frames_path = "frames"
shutil.rmtree(
    frames_path,
)
os.makedirs(frames_path, exist_ok=True)

# Read CSV
csv_file = "yt-videos.csv"
urls_df = pd.read_csv(csv_file)
urls = urls_df["url"].tolist()

for url in urls:
    try:
        print(f"Processing: {url}")
        video_path = download_video(url, videos_path)
        extract_frames(video_path=video_path, output_path=frames_path, frame_rate=1)
        os.remove(video_path)
        time.sleep(0.5)  # Wait for 500 ms to avoid a block from YouTube
    except Exception as e:
        print(f"Failed to process {url}: {e}")

shutil.rmtree(
    videos_path,
)
