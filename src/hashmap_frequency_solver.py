"""
    Method 4: Find anagrams and subanagrams of a given word using hash map 
    with letter frequency count.
    
    This program reads a word list from a file, preprocesses it to cound the frequency
    of each letter in the word, and then finds all anagrams and sub-anagrams of a given word.
    
    The program uses the following steps:
    1. Preprocess the word list file to create a dictionary mapping sorted letters to words.
    2. Count the frequency of each letter in the input word.
    3. Find anagrams and sub-anagrams based on the letter counts.
    4. Print the anagrams and sub-anagrams of the input word.
    
    Author: Sai Sharan Thirunagari
    Date: 11-15-2024
    
"""

from typing import Dict, List, Tuple


class HashMapFrequencySolver:
    """
    A solver to find anagrams and sub-anagrams of a given word using a hash map
    with letter frequency counts.

    This class assumes that the hash map (mapping words to letter frequencies)
    is loaded externally and passed during initialization.

    Attributes:
        word_letter_counts (Dict[str, Dict[str, int]]): A dictionary mapping words to their
        respective letter frequency counts.

    Methods:
        find_anagrams_and_sub_anagrams(word: str) -> Tuple[List[str], List[str]]:
            Finds anagrams and sub-anagrams of the given word.
    """

    def __init__(self, word_letter_counts: Dict[str, Dict[str, int]]) -> None:
        """
        Initialize the HashMapFrequencySolver with a preloaded hash map.

        Args:
            word_letter_counts (Dict[str, Dict[str, int]]): A dictionary mapping words
            to their letter frequency counts.
        """
        self.word_letter_counts: Dict[str, Dict[str, int]] = word_letter_counts

    def find_anagrams_and_sub_anagrams(self, word: str) -> Tuple[List[str], List[str]]:
        """
        Find anagrams and sub-anagrams of the input word using the preloaded hash map.

        Anagrams are words that use all the letters in the input word exactly once.
        Sub-anagrams are words formed by using a subset of the letters in the input word.

        Args:
            word (str): The input word to find anagrams and sub-anagrams.

        Returns:
            Tuple[List[str], List[str]]: A tuple containing two lists:
                - A list of anagrams of the input word.
                - A list of sub-anagrams of the input word.
        """
        word = word.lower()
        input_letter_counts: Dict[str, int] = self._get_letter_counts(word)
        input_letter_counts_tuple = tuple(sorted(input_letter_counts.items()))
        # anagrams: List[str] = self.word_letter_counts.get(input_letter_counts, [])
        # Find exact anagrams (key match)
        anagrams = self.word_letter_counts.get(input_letter_counts_tuple, [])

        sub_anagrams: List[str] = []
        # for candidate, letter_counts in self.word_letter_counts.items():
        #     if len(candidate) > len(word):
        #         continue

        #     is_anagram: bool = True
        #     for letter, count in letter_counts.items():
        #         if input_letter_counts.get(letter, 0) < count:
        #             is_anagram = False
        #             break

        #     if is_anagram:
        #         if len(candidate) == len(word):
        #             anagrams.append(candidate)
        #         else:
        #             sub_anagrams.append(candidate)
        for candidate_counts_tuple, candidate_words in self.word_letter_counts.items():
            candidate_letter_counts = dict(candidate_counts_tuple)
            print(candidate_counts_tuple, candidate_words, candidate_letter_counts)
            # Check if candidate is a subset of the input word
            if all(
                input_letter_counts.get(letter, 0) >= count
                for letter, count in candidate_letter_counts.items()
            ):
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
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        return letter_counts
