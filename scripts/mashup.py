from moviepy.editor import concatenate_audioclips, AudioFileClip
import os

def mashup_audios(output_file):
    audio_dir = "./audios"
    output_path = f"./{output_file}"
    songs = []
    for file_name in os.listdir(audio_dir):
        if file_name.endswith('.mp3'):
            songs.append(AudioFileClip(os.path.join(audio_dir, file_name)))
    
    if not songs:
        print("No files found to create a mashup.")
        return
    
    mashup_song = concatenate_audioclips(songs)
    mashup_song.write_audiofile(output_path)


