import streamlit as st
from modules.lyrics_processor import clean_lyrics, detect_language
from modules.voice_generator import generate_voice
from modules.music_generator import generate_music
from modules.mixer import mix_tracks
from modules.utils import ensure_output_folder

import os

st.set_page_config(page_title="Lyrics to Music Generator", layout="centered")

ensure_output_folder()

st.title("🎵 Lyrics to Music Generator (Hindi Bhajan, Romantic, etc.)")
st.markdown("Generate a full song from your lyrics using AI.\n\nSupports **Hindi & Indian languages** 🎤")

lyrics = st.text_area("✍️ Enter Your Lyrics", height=200)

genre = st.selectbox("🎼 Choose Music Style", ["Devotional Bhajan", "Romantic", "Calm Instrumental", "Energetic Dance"])

voice_style = st.selectbox("🧑‍🎤 Choose Singing Voice", [
    "Female (Soft)",
    "Male (Soft)",
    "Child (Girl)",
    "Old Man",
    "Old Woman",
    "Excited",
    "Calm"
])

duration = st.slider("⏱️ Song Duration (seconds)", min_value=5, max_value=30, value=12)

generate_btn = st.button("🎶 Generate Song")

if generate_btn and lyrics.strip():
    with st.spinner("Processing your song... 🎧"):
        cleaned = clean_lyrics(lyrics)
        lang = detect_language(cleaned)

        music_prompt = f"A {genre.lower()} with Indian instruments like tabla, flute, tanpura."
        music_path = generate_music(prompt=music_prompt, duration=duration)

        voice_map = {
            "Female (Soft)": "v2/hi_speaker_1",
            "Male (Soft)": "v2/hi_speaker_2",
            "Child (Girl)": "v2/en_speaker_9",
            "Old Man": "v2/en_speaker_7",
            "Old Woman": "v2/en_speaker_5",
            "Excited": "v2/en_speaker_6",
            "Calm": "v2/en_speaker_3",
        }
        voice_preset = voice_map.get(voice_style, "v2/hi_speaker_1")

        vocals_path = generate_voice(lyrics=cleaned, voice_preset=voice_preset)

        final_song_path = mix_tracks(vocals_path, music_path)

    st.success("✅ Your song is ready!")
    st.audio(final_song_path, format="audio/mp3")
    with open(final_song_path, "rb") as f:
        st.download_button("⬇️ Download Song", f, file_name="generated_song.mp3", mime="audio/mp3")
else:
    st.info("Please enter your lyrics above to begin.")