import cv2

def extract_frames(video_path, output_path, frame_rate):
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
                # Save the extracted frame to the output path
                cv2.imwrite(f"{output_path}/frame_{frame_count}.jpg", frame)
        
        # Increment the frame count
        frame_count += 1
    
    # Release the video file
    video.release()

# Example usage
video_path = "video.mp4"
output_path = "output"
frame_rate = 1  # Extract one frame per second

extract_frames(video_path, output_path, frame_rate)
