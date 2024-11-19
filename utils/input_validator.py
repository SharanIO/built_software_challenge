"""
Input Validator: Utility to validate and sanitize input words for the Anagram Solver.

This module ensures that input words:
- Contain only alphabetic characters.
- Are converted to lowercase for consistent processing.
- Are non-empty after sanitization.

Raises:
    ValueError: If the sanitized word is empty.
"""

def validate_input_word(word: str) -> str:
    """
    Validate and sanitize the input word.

    Args:
        word (str): The input word to validate.

    Returns:
        str: The sanitized word, containing only lowercase alphabetic characters.

    Raises:
        ValueError: If the word is empty after sanitization.
    """
    # Remove non-alphabetic characters and convert to lowercase
    sanitized_word = ''.join(filter(str.isalpha, word)).lower()
    
    # Check if the sanitized word is empty
    if not sanitized_word:
        raise ValueError("The input word must contain at least one alphabetic character.")
    
    return sanitized_word
