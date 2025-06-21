import subprocess
import os

def split_video_ffmpeg(input_path, output_folder, duration):
    os.makedirs(output_folder, exist_ok=True)

    # Get video duration (in seconds)
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', input_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    total_duration = float(result.stdout)
    
    part = 0
    start = 0

    while start < total_duration:
        output_path = os.path.join(output_folder, f"clip_{part + 1}.mp4")
        command = [
            'ffmpeg',
            '-ss', str(start),
            '-i', input_path,
            '-t', str(duration),
            '-c', 'copy',
            output_path
        ]
        subprocess.run(command)
        print(f"✅ Saved: {output_path}")
        start += duration
        part += 1

    print("🎬 All clips created.")

# Example usage:
inp = r"D:\D\Projects\Youtube\clips\clip_1.mp4"
out = r"D:\D\Projects\Youtube\video_clip"
split_video_ffmpeg(inp, out, 60)
