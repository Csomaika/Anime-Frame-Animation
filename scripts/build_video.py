from pathlib import Path
import subprocess

FPS = 10
FRAMES = Path("frames")
OUTPUT = Path("output")
OUTPUT.mkdir(exist_ok=True)

# Expected names: frame_0001.png ... frame_0050.png
cmd = [
    "ffmpeg", "-y",
    "-framerate", str(FPS),
    "-start_number", "1",
    "-i", str(FRAMES / "frame_%04d.png"),
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    str(OUTPUT / "anime_animation.mp4"),
]

print("Building 5-second animation at 10 FPS...")
subprocess.run(cmd, check=True)
print("Done: output/anime_animation.mp4")
