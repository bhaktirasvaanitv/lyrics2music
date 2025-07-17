import os
import torchaudio
from bark import generate_audio, preload_models

preload_models()

def generate_voice(lyrics: str, voice_preset="v2/hi_speaker_1") -> str:
    audio_array = generate_audio(lyrics, history_prompt=voice_preset)
    output_path = "output/vocals.wav"
    torchaudio.save(output_path, audio_array[None, :], sample_rate=24000)
    return output_path