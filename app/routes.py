from flask import request, jsonify
from app import app
from app.img_to_text import img_to_text
from app.audio_to_text import audio_to_text


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the API"})


@app.route("/img_to_text", methods=["POST"])
def img_to_text_route():
    return img_to_text(request)


@app.route("/audio_to_text", methods=["POST"])
def audio_to_text_route():
    return audio_to_text(request)
