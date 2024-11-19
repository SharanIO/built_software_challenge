"""
HashMapFrequencySolver: Find anagrams and sub-anagrams using a hash map with letter frequency counts.

This class provides a solution for efficiently finding anagrams and sub-anagrams
of a given word by leveraging a hash map that maps words to their letter frequency counts.

Features:
1. Finds anagrams by matching the letter frequency of the input word.
2. Finds sub-anagrams by identifying words that match a subset of the input word's letter frequencies.

Limitations:
- The preloaded hash map must be generated externally and passed during initialization.

Author: Sai Sharan Thirunagari
Date: 11-15-2024
"""

from typing import Dict, List, Tuple


class HashMapFrequencySolver:
    """
    A solver to find anagrams and sub-anagrams using a hash map with letter frequency counts.

    Attributes:
        word_letter_counts (Dict[Tuple[Tuple[str, int], ...], List[str]]): 
            A dictionary mapping sorted letter frequency tuples to corresponding words.

    Methods:
        find_anagrams_and_sub_anagrams(word: str) -> Tuple[List[str], List[str]]:
            Finds anagrams and sub-anagrams for a given input word.
    """

    def __init__(self, word_letter_counts: Dict[Tuple[Tuple[str, int], ...], List[str]]) -> None:
        """
        Initialize the HashMapFrequencySolver with a preloaded hash map.

        Args:
            word_letter_counts (Dict[Tuple[Tuple[str, int], ...], List[str]]): 
                A dictionary mapping sorted letter frequency tuples to corresponding words.
        """
        self.word_letter_counts: Dict[Tuple[Tuple[str, int], ...], List[str]] = word_letter_counts

    def find_anagrams_and_sub_anagrams(self, word: str) -> Tuple[List[str], List[str]]:
        """
        Find anagrams and sub-anagrams of the input word using the preloaded hash map.

        Anagrams are words that use all the letters in the input word exactly once.
        Sub-anagrams are words formed by using a subset of the letters in the input word.

        Steps:
        1. Normalize the input word to lowercase.
        2. Generate the letter frequency dictionary for the input word.
        3. Find exact anagrams by matching the sorted frequency tuple.
        4. Iterate through the hash map to find sub-anagrams by comparing frequency subsets.

        Args:
            word (str): The input word to analyze.

        Returns:
            Tuple[List[str], List[str]]:
                - A list of anagrams of the input word.
                - A list of sub-anagrams of the input word (excluding exact anagrams).
        """
        word = word.lower()  # Normalize input to lowercase
        input_letter_counts = self._get_letter_counts(word)  # Frequency of input word letters
        input_letter_counts_tuple = tuple(sorted(input_letter_counts.items()))  # Convert to sorted tuple

        # Find exact anagrams (exact key match)
        anagrams = self.word_letter_counts.get(input_letter_counts_tuple, [])

        sub_anagrams: List[str] = []
        # Find sub-anagrams (subset matches)
        for candidate_counts_tuple, candidate_words in self.word_letter_counts.items():
            candidate_letter_counts = dict(candidate_counts_tuple)
            # Check if candidate is a subset of the input word
            if all(
                input_letter_counts.get(letter, 0) >= count
                for letter, count in candidate_letter_counts.items()
            ):
                # Exclude exact anagrams
                if candidate_counts_tuple != input_letter_counts_tuple:
                    sub_anagrams.extend(candidate_words)

        return anagrams, sub_anagrams

    @staticmethod
    def _get_letter_counts(word: str) -> Dict[str, int]:
        """
        Count the frequency of each letter in the input word.

        Args:
            word (str): The input word.

        Returns:
            Dict[str, int]: A dictionary mapping each letter to its frequency in the word.
        """
        letter_counts: Dict[str, int] = {}
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1  # Increment the count for each letter
        return letter_counts
