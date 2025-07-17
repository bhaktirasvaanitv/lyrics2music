import re

def clean_lyrics(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def detect_language(text: str) -> str:
    if re.search(r'[ऀ-ॿ]', text):
        return "hindi"
    return "english"