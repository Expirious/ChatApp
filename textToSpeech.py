from TTS.api import TTS  # Coqui TTS library
from pathlib import Path

# Load the model (for Coqui TTS)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# Run text-to-speech and save to a file
try:
    tts.tts_to_file(text="Hello World", file_path="audio.wav")
except Exception as e:
    print(e)