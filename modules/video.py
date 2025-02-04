import cv2
import os
import hashlib
import numpy as np
from moviepy import ImageSequenceClip

def create_video_from_images(image_folder="images", output_video="videos/output_video.mp4", fps=30):
    """Create MP4 with lossless encoding using MoviePy"""
    os.makedirs(os.path.dirname(output_video), exist_ok=True)
    
    # Get sorted list of images
    image_files = sorted([os.path.join(image_folder, f) 
                         for f in os.listdir(image_folder) if f.endswith('.png')],
                        key=lambda x: int(os.path.basename(x).split('.')[0]))

    # Create video with lossless settings
    clip = ImageSequenceClip(image_files, fps=fps)
    
    # FFmpeg parameters for lossless encoding
    clip.write_videofile(
        output_video,
        codec='libx264rgb',
        preset='ultrafast',
        ffmpeg_params=[
            '-crf', '0',           # Lossless
            '-color_range', '2',   # Full color range
            '-pix_fmt', 'bgr24'    # Match OpenCV's BGR format
        ]
    )




def extract_frames_from_video(video_path="videos/output_video.mp4", output_folder="extracted_frames"):
    """Extract frames with OpenCV and hash verification"""
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break
        
        output_path = os.path.join(output_folder, f"{frame_count}.png")
        cv2.imwrite(output_path, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        
        with open(output_path, 'rb') as f:
            current_hash = hashlib.sha256(f.read()).hexdigest()
        print(f"Frame {frame_count:04d} hash: {current_hash}")
        
        frame_count += 1

    cap.release()


