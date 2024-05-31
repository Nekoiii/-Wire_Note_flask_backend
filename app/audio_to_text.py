from flask import jsonify
import torch
import librosa
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


def audio_to_text(request):
    print("Begin audio_to_text.")
    audio_file = request.files["file"]
    audio, rate = librosa.load(audio_file, sr=16000)

    input_values = processor(
        audio, return_tensors="pt", sampling_rate=16000
    ).input_values
    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    return jsonify({"transcription": transcription})
