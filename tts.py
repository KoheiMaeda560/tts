"""
This script converts text files to audio files (.mp3).

Usage:
python tts.py filename1.txt

Options:
- VOICE: Specifies the voice type to use. Default is "en-US-AndrewNeural".

- OUTPUT_DIR: Specifies the output directory. Default is "output".

- CHUNK_SIZE: Specifies the chunk size for processing files. Default is 10.

- MAX_CONCURRENT_TASKS: Specifies the number of concurrent tasks. Default is 5.

Examples:
python tts.py my_text.txt
python tts.py ./input/*.txt
"""

from typing import List

import edge_tts
import asyncio
import os
import sys
import glob

# set a voice from the voice list -- $edge-tts --list-voices
VOICE = "en-US-AndrewNeural"

OUTPUT_DIR = "output"
CHUNK_SIZE = 10  # chunk size
MAX_CONCURRENT_TASKS = 5  # maximum concurrent tasks

async def generate_speech(text: str, output_path: str):
    try:
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(output_path)
        print(f"Saved audio file: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def process_file(filename: str):
    """Reads a file and generates speech."""
    base = os.path.splitext(filename)[0]
    output_path = os.path.join(OUTPUT_DIR, os.path.basename(base) + ".mp3")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    await generate_speech(text, output_path)

async def process_chunk(files: List[str]):
    """Processes files in chunks."""
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)  # limit concurrent tasks with a semaphore

    async def process_file_with_semaphore(filename: str):
        async with semaphore:
            await process_file(filename)

    tasks = [process_file_with_semaphore(filename) for filename in files]
    await asyncio.gather(*tasks)

async def main(files: List[str]):
    """Divides files into chunks and processes them."""
    for i in range(0, len(files), CHUNK_SIZE):
        chunk = files[i:i + CHUNK_SIZE]
        print(f"Processing chunk {i // CHUNK_SIZE + 1} of {len(files) // CHUNK_SIZE + (1 if len(files) % CHUNK_SIZE != 0 else 0)}...")  # display progress
        await process_chunk(chunk)

if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)  # Create output directory if it doesn't exist
    args = sys.argv[1:]
    expanded_files = []
    for arg in args:
        expanded_files.extend(glob.glob(arg, recursive=True))

    if not expanded_files:
        print("No files specified for processing.")
    else:
        asyncio.run(main(expanded_files))