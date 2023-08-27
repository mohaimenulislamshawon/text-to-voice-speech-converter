from flask import Flask, render_template, request, send_file, Response
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        language = request.form.get("language")

        if text and language:
            tts = gTTS(text, lang=language)
            output_file = "output.mp3"
            tts.save(output_file)

            return render_template("index.html", message="Conversion successful.", audio=output_file)
        else:
            return render_template("index.html", error="Please provide both text and language.")
    
    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    return send_file(filename, as_attachment=True)

@app.route("/play/<filename>")
def play(filename):
    audio_file_path = os.path.join(os.getcwd(), filename)
    return Response(open(audio_file_path, "rb"), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)

