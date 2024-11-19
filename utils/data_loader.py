"""
Data Loader: Utility for loading a word list from a file.

This module provides a function to load a list of words from a specified file.
The words are assumed to be separated by whitespace (e.g., spaces, newlines).

Raises:
    FileNotFoundError: If the specified file does not exist.

Example Usage:
    from utils.data_loader import load_word_list

    word_list = load_word_list("data/words_alpha.txt")
"""

from typing import List


def load_word_list(file_path: str) -> List[str]:
    """
    Load a word list from a specified file.

    Each word in the file is separated by whitespace (spaces, newlines, etc.).
    The function reads the file, splits its content into individual words, 
    and returns them as a list.

    Args:
        file_path (str): Path to the file containing the word list.

    Returns:
        List[str]: A list of words loaded from the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words: List[str] = file.read().split()
            return words
    except FileNotFoundError:
        print(
            f"Error: Word list file not found at '{file_path}'. "
            "Please ensure the file exists and the path is correct."
        )
        exit(1)
