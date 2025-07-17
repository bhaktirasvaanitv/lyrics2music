from pydub import AudioSegment

def mix_tracks(vocals_path: str, music_path: str, output_path: str = "output/final_song.mp3") -> str:
    vocals = AudioSegment.from_file(vocals_path)
    music = AudioSegment.from_file(music_path)

    if len(music) < len(vocals):
        music = music * (len(vocals) // len(music) + 1)
    music = music[:len(vocals)]

    combined = music - 3
    combined = combined.overlay(vocals)

    combined.export(output_path, format="mp3")
    return output_path