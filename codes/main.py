from moviepy.video.io.VideoFileClip import VideoFileClip
import cv2
import os

def split_video(inp, out_dr, duration):
    # Load the video file
    video = VideoFileClip(inp)
    
    # Get total duration of the video in seconds
    video_len = int(video.duration)

    # Calculate how many clips will be created
    clip_count = (video_len // duration) + (1 if video_len % duration else 0)

    # Ensure output directory exists
    os.makedirs(out_dr, exist_ok=True)

    # Split the video into equal parts
    for i in range(clip_count):
        start_time = i * duration
        end_time = min((i + 1) * duration, video_len)

        # Extract subclip
        sub_clip = video.subclipped(start_time, end_time)

        # Define output path
        out_file = os.path.join(out_dr, f'clip_{i + 1}.mp4')

        # Write subclip to file
        sub_clip.write_videofile(out_file, codec="libx264", audio_codec="aac")
        print(f"✅ Saved: {out_file}")

    print("🎬 Video splitting complete!")

# Example usage:
inp = r"D:\D\Projects\Youtube\clips\clip_1.mp4"
out_dir = r"D:\D\Projects\Youtube\video_clip"
split_video(inp, out_dir, 60)
