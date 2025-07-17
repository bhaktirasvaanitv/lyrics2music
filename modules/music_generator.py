import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('facebook/musicgen-small')

def generate_music(prompt: str, duration: int = 10) -> str:
    model.set_generation_params(duration=duration)
    output = model.generate([prompt])
    output_path = "output/instrumental"
    audio_write(output_path, output[0].cpu(), model.sample_rate, format="wav")
    return output_path + ".wav"