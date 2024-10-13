from moviepy.editor import AudioFileClip
import os

def trim(time):
    input_dir = "./audios"
    output_dir = "./audios"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.mp3'):
            audio_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            
            with AudioFileClip(audio_path) as audio:
                if time > audio.duration:
                    print("Specified duration exceeds song duration.")
                    time = audio.duration 
                
                trimmed_audio = audio.subclip(0, min(time, audio.duration)) 
                
            
                trimmed_audio.write_audiofile(output_path)
                print(f"Trimmed {file_name} and saved to {output_path}")
            
    print("All audio files have been trimmed.")

