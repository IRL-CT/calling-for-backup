import cv2
import os
import numpy as np
from pathlib import Path

def anonymize_faces_in_video(video_path, output_folder, blur_strength=51):
    """
    Extract frames from video and anonymize faces
    """
    # Load face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Open video
    cap = cv2.VideoCapture(str(video_path))
    
    if not cap.isOpened():
        print(f"Error opening video: {video_path}")
        return
    
    # Create output folder for this video
    video_name = video_path.stem
    video_output_folder = output_folder / video_name
    video_output_folder.mkdir(exist_ok=True)
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        # Apply blur to each detected face
        for (x, y, w, h) in faces:
            # Extract face region
            face_region = frame[y:y+h, x:x+w]
            
            # Apply Gaussian blur to face region
            blurred_face = cv2.GaussianBlur(face_region, (blur_strength, blur_strength), 0)
            
            # Replace original face with blurred version
            frame[y:y+h, x:x+w] = blurred_face
        
        # Save frame
        frame_filename = video_output_folder / f"frame_{frame_count:06d}.jpg"
        cv2.imwrite(str(frame_filename), frame)
        
        frame_count += 1
        
        if frame_count % 100 == 0:
            print(f"Processed {frame_count} frames from {video_name}")
    
    cap.release()
    print(f"Completed {video_name}: {frame_count} frames processed")

def process_video_folder(input_folder, output_folder, blur_strength=51):
    """
    Process all videos in a folder
    """
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)
    
    # Supported video formats
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
    
    # Find all video files
    video_files = []
    for ext in video_extensions:
        video_files.extend(input_path.glob(f"*{ext}"))
        video_files.extend(input_path.glob(f"*{ext.upper()}"))
    
    if not video_files:
        print(f"No video files found in {input_folder}")
        return
    
    print(f"Found {len(video_files)} video files")
    
    for video_file in video_files:
        print(f"Processing: {video_file.name}")
        anonymize_faces_in_video(video_file, output_path, blur_strength)
    
    print("All videos processed!")

# Usage example
if __name__ == "__main__":
    # Set your paths here
    INPUT_FOLDER = "path/to/your/video/folder"
    OUTPUT_FOLDER = "path/to/output/anonymized_frames"
    
    # Adjust blur strength (must be odd number, higher = more blur)
    BLUR_STRENGTH = 51
    
    process_video_folder(INPUT_FOLDER, OUTPUT_FOLDER, BLUR_STRENGTH)
