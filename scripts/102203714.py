import os
import sys
from search_title import download
from convert_to_audio import convert_all_videos_to_audio
from trim_audio import trim
from mashup import mashup_audios
from zip_file import create_rar

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)
    
    singer_name = sys.argv[1]
    number_of_videos = int(sys.argv[2])
    audio_duration = int(sys.argv[3])
    output_file_name = sys.argv[4]
    
    output_rar = output_file_name.replace(".mp3",".rar")
    
    print(f"Downloading {number_of_videos} videos of {singer_name}...")
    download(singer_name, number_of_videos)

    print("Converting videos to audio...")
    convert_all_videos_to_audio()

    print(f"Trimming the audio files to {audio_duration} seconds each...")
    trim(audio_duration)

    print("Merging audio files into a mashup...")
    mashup_audios(output_file_name)

    print("Zipping the mashup file...")
    create_rar(output_file_name, output_rar)

    print("Mashup process completed successfully!")
    
if __name__ == "__main__":
    main()