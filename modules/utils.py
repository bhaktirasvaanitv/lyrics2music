import os

def ensure_output_folder():
    if not os.path.exists("output"):
        os.makedirs("output")