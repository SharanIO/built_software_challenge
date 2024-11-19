"""
Brute Force Solver: Find anagrams and sub-anagrams of a given word.

This program compares an input word against a list of words and identifies:
1. Anagrams: Words that have exactly the same letters as the input word.
2. Sub-anagrams: Words that use a subset of the letters in the input word.

Steps:
1. Count the frequency of letters in the input word.
2. Compare each word in the word list to determine if it is an anagram or sub-anagram.
3. Return lists of anagrams and sub-anagrams.

Complexity:
- Time complexity: O(N * M), where N is the number of words in the list and M is the average word length.

Author: Sai Sharan Thirunagari
Date: 11-15-2024
"""

from collections import Counter
from typing import List, Tuple


class BruteForceAnagramSolver:
    """
    A solver for finding anagrams and sub-anagrams using a brute-force approach.

    This solver compares the letter frequencies of an input word against a word list
    to identify:
    - Anagrams: Words with exactly the same letters as the input word.
    - Sub-anagrams: Words that can be formed using a subset of the input word's letters.
    """

    def __init__(self, word_list: List[str]) -> None:
        """
        Initialize the solver with a list of words.

        Args:
            word_list (List[str]): A list of valid words to compare against.
        """
        if not word_list:
            raise ValueError("Word list cannot be empty.")
        self.words = word_list

    @staticmethod
    def _get_letter_count(word: str) -> Counter:
        """
        Count the frequency of each letter in a word.

        Args:
            word (str): The input word.

        Returns:
            Counter: A Counter object mapping each letter to its frequency.
        """
        return Counter(word)

    def find_anagrams_and_subanagrams(self, word_input: str) -> Tuple[List[str], List[str]]:
        """
        Find anagrams and sub-anagrams of the input word.

        Steps:
        1. Convert the input word to lowercase for case-insensitive comparison.
        2. Calculate the letter frequency of the input word.
        3. Iterate through the word list to identify anagrams and sub-anagrams.

        Args:
            word_input (str): The input word to analyze.

        Returns:
            Tuple[List[str], List[str]]:
                - A list of anagrams of the input word.
                - A list of sub-anagrams of the input word.
        """
        # Normalize the input word to lowercase
        word_input = word_input.lower()

        # Calculate the letter frequency of the input word
        input_letter_counts = self._get_letter_count(word_input)

        # Initialize lists to store results
        anagrams: List[str] = []
        sub_anagrams: List[str] = []

        for word in self.words:
            # Normalize each word in the list
            word = word.lower()
            word_letter_counts = self._get_letter_count(word)

            # Check if the word is an anagram
            if len(word) == len(word_input) and word_letter_counts == input_letter_counts:
                anagrams.append(word)

            # Check if the word is a sub-anagram
            elif len(word) < len(word_input) and all(
                word_letter_counts[letter] <= input_letter_counts[letter]
                for letter in word_letter_counts
            ):
                sub_anagrams.append(word)

        return anagrams, sub_anagrams
