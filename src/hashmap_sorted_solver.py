"""
HashMapSolver: Find anagrams and sub-anagrams using a hash map.

This class provides a solution for efficiently finding anagrams and sub-anagrams
of a given word by leveraging a hash map where keys are sorted letters of words,
and values are lists of corresponding words.

Features:
1. Creates a hash map from a word list.
2. Finds anagrams by matching the sorted form of the input word.
3. Finds sub-anagrams by generating all possible subsets of the input word's letters.

Limitations:
- Generating all subsets for long input words can be computationally expensive.

Author: Sai Sharan Thirunagari
Date: 11-15-2024
"""

from typing import List, Tuple, Dict, Set


class HashMapSolver:
    """
    A class to find anagrams and sub-anagrams using a hash map.

    This solver uses:
    - A hash map with sorted letters as keys and lists of words as values.
    - A method to sort strings.
    - A method to generate all subsets of a string for sub-anagrams.
    """

    def __init__(self, words_map: Dict[str, List[str]]) -> None:
        """
        Initialize the solver with a hash map of words.

        Args:
            words_map (Dict[str, List[str]]): A dictionary mapping sorted letters
                                              to lists of corresponding words.
        """
        self.word_map: Dict[str, List[str]] = words_map

    def _sort_string(self, word: str) -> str:
        """
        Sort the characters in a string and return the sorted string.

        Args:
            word (str): The input string to be sorted.

        Returns:
            str: A new string with characters sorted in ascending order.
        """
        return ''.join(sorted(word))  # Use Python's built-in sorted for efficiency

    def _get_combinations(self, letters: str) -> List[str]:
        """
        Generate all non-empty subsets of the input letters.

        This method uses bitwise operations to generate subsets:
        - Each bit in a number represents whether to include a letter in the subset.
        - Total combinations = 2^n - 1, where n is the length of the string.

        Args:
            letters (str): Input string of letters.

        Returns:
            List[str]: A list of all non-empty subsets of the letters.
        """
        combinations = []
        n = len(letters)
        total_combinations = 2 ** n
        for i in range(1, total_combinations):  # Skip 0 to avoid the empty subset
            combo = ''.join(letters[j] for j in range(n) if i & (1 << j))
            combinations.append(combo)
        return combinations

    def find_anagrams_and_subanagrams(self, word: str) -> Tuple[Set[str], Set[str]]:
        """
        Identify anagrams and sub-anagrams for a given word using the hash map.

        Steps:
        1. Sort the input word to find exact anagrams in the hash map.
        2. Generate all subsets of the input word's letters.
        3. For each subset, find matching sub-anagrams in the hash map.

        Args:
            word (str): The input word to analyze.

        Returns:
            Tuple[Set[str], Set[str]]:
                - A set of anagrams of the input word.
                - A set of sub-anagrams of the input word.
        """
        word = word.lower()  # Normalize input to lowercase
        sorted_input_word = self._sort_string(word)

        # Find exact anagrams
        anagrams: Set[str] = set(self.word_map.get(sorted_input_word, []))

        # Find sub-anagrams
        sub_anagrams: Set[str] = set()
        combos = self._get_combinations(word)  # Generate all subsets

        for combo in combos:
            sorted_combo = self._sort_string(combo)
            # Exclude exact matches
            if sorted_combo == sorted_input_word:
                continue
            if sorted_combo in self.word_map:
                sub_anagrams.update(self.word_map[sorted_combo])

        return anagrams, sub_anagrams
