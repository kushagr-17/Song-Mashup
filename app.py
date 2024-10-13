from flask import Flask, request, render_template
from scripts.search_title import download
from scripts.send_mail import send_email
from scripts.convert_to_audio import convert_all_videos_to_audio
from scripts.trim_audio import trim
from scripts.mashup import mashup_audios
from scripts.zip_file import create_rar
import os

app = Flask(__name__, 
            static_folder=r"scripts/static", 
            template_folder=r"scripts/templates")

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        singer_name = request.form['singer_name']
        num_videos = int(request.form['num_videos'])
        duration = int(request.form['duration'])
        email = request.form['email_id']

        download(singer_name, num_videos)

        convert_all_videos_to_audio()

        trim(duration)

        output_file = "mashup_song.mp3"
        mashup_audios(output_file)

        output_rar = "mashup_song.rar"
        create_rar(output_file, output_rar)

        subject = "Your Mashup File"
        body = "Hey there! Kindly see your requested mashup file."
        send_email(email, subject, body, output_rar)

        return "Mashup created and sent to your email!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
