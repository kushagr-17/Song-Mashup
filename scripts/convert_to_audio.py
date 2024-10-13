import os
from moviepy.editor import VideoFileClip

def convert_all_videos_to_audio():
    video_folder = "./videos"
    audio_folder = "./audios"

    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(video_folder, filename)
            audio_output_path = os.path.join(audio_folder, filename.replace(".mp4", ".mp3"))

            video_clip = VideoFileClip(video_path)
            video_clip.audio.write_audiofile(audio_output_path)
            video_clip.close()


