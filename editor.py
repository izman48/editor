#!/usr/bin/env python3

from moviepy.editor import VideoFileClip
import typer

def trimClip(name: str, start: int = None, end: int = None, result_name: str = "output.mp4", fps: int = 25, compress: bool = True):
    codec = "libx264"
    if compress:
        codec = "h264_nvenc"
    video = VideoFileClip(name).subclip(start, end)
    video.write_videofile(result_name, fps=fps, codec=codec)  # Many options...

    video.reader.close()
    del video


def main():
    typer.run(trimClip)


if __name__ == "__main__":
    main()