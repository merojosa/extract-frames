import os
import cv2

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

# Example usage
videos_directory = "videos"
output_path = "output"
frame_rate = 1  # Extract one frame per second

# Iterate over all video files in the directory
for filename in os.listdir(videos_directory):
    if filename.endswith(".mkv"):  # Modify the condition if using a different video format
        video_path = os.path.join(videos_directory, filename)
        extract_frames(video_path, output_path, frame_rate)
