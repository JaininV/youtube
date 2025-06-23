from text_clean import escape_font_path

import os
import math
import subprocess
from tqdm import tqdm

def split_video_with_labels(input_path, output_dir, clip_length=60):
    # Get video duration
    ffmpeg_path = 'D:/D/Projects/ffmpeg-7.1.1-full_build/bin/ffmpeg.exe'
    file_name = os.path.basename(input_path)
    file_name = os.path.splitext(file_name)[0]

    
    result = subprocess.run(
        [ffmpeg_path, '-i', input_path],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    

    for line in result.stderr.splitlines():
        if "Duration" in line:
            time_str = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = map(float, time_str.split(":"))
            total_duration = int(h * 3600 + m * 60 + s)
            break
    else:
        print("Could not determine video duration.")

    # Create output directory
    output_dir = output_dir + f"/{file_name}"
    os.makedirs(output_dir, exist_ok=True)

    # Total number of parts
    num_parts = math.ceil(total_duration / clip_length)

    for i in tqdm(range(num_parts), desc="Splitting video"):
        start = i * clip_length
        out_file = os.path.join(output_dir, f"{file_name}_part_{i+1}.mp4").replace("\\", "/")
        label = f"Part {i+1}"

        # for font style
        FONT   = 'D:/D/Projects/Youtube/font_style/apercumovistarbold.ttf'
        escaped_font = escape_font_path(FONT)
        drawtext_filter = (
            f"drawtext=fontfile='{escaped_font}':"
            f"text='{label}':"
            f"x=10:y=10:"
            f"fontsize=50:fontcolor=black:box=1:boxcolor=white@0.5"
        )

        # FFmpeg command
        command = [
            ffmpeg_path,
            "-y",  # overwrite without asking
            "-ss", str(start),
            "-t", str(clip_length),
            "-i", input_path,
            "-vf", drawtext_filter,
            "-preset", "ultrafast",
            "-c:a", "copy",
            out_file
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    return {
        'msg': 'Process completed.'
    }


