# utils/data_loader.py
from typing import List

def load_word_list(file_path: str) -> List[str]:
    """Load a word list from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words: List[str] = file.read().split()
            return words
    except FileNotFoundError:
        print(
            'Word list file not found. Please make sure the file exists in the data directory.')
        exit(1)
