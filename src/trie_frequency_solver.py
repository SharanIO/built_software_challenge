"""
Trie Frequency Solver: Find anagrams and sub-anagrams using a Frequency Trie.

This module implements a solver to efficiently find anagrams and sub-anagrams
of a given word using a frequency-based Trie.

Features:
1. Initializes a Frequency Trie with preloaded data.
2. Searches for anagrams (words that match all letters in the input exactly).
3. Searches for sub-anagrams (words that use a subset of the input letters).

Author: Sai Sharan Thirunagari
Date: 11-15-2024
"""

from typing import List, Tuple, Dict, Set
from utils.frequency_trie import TrieNode, FrequencyTrie


class TrieFrequencySolver(FrequencyTrie):
    """
    A solver to find anagrams and sub-anagrams using a Frequency Trie.

    This class extends the FrequencyTrie to implement methods for efficiently
    finding anagrams and sub-anagrams of a given word. It leverages the Trie
    structure to limit the search space based on letter frequencies.
    """

    def __init__(self, frequency_trie: FrequencyTrie) -> None:
        """
        Initialize the solver with a preloaded Frequency Trie.

        Args:
            frequency_trie (FrequencyTrie): A preloaded Frequency Trie instance.
        """
        super().__init__()
        self.root = frequency_trie.root

    def find_anagrams_and_subanagrams(self, word: str) -> Tuple[List[str], List[str]]:
        """
        Find all anagrams and sub-anagrams of the given word.

        Steps:
        1. Convert the input word to lowercase for uniform comparison.
        2. Generate a frequency dictionary for the input word.
        3. Recursively search the Trie for matching words.

        Args:
            word (str): The input word.

        Returns:
            Tuple[List[str], List[str]]: 
                - A list of anagrams of the input word.
                - A list of sub-anagrams of the input word.
        """
        word = word.lower()  # Normalize input to lowercase
        freq = self._get_frequency_dict(word)  # Generate letter frequency dictionary
        anagrams: Set[str] = set()
        sub_anagrams: Set[str] = set()

        # Start recursive search from the root
        self._search_anagrams_and_sub_anagrams(
            current=self.root,
            freq=freq,
            prefix="",
            anagrams=anagrams,
            sub_anagrams=sub_anagrams,
            word_length=len(word)
        )

        # Exclude the original word from sub-anagrams
        sub_anagrams.discard(word)

        return list(anagrams), list(sub_anagrams)

    def _search_anagrams_and_sub_anagrams(
        self,
        current: TrieNode,
        freq: Dict[str, int],
        prefix: str,
        anagrams: Set[str],
        sub_anagrams: Set[str],
        word_length: int
    ) -> None:
        """
        Recursively search for anagrams and sub-anagrams in the Trie.

        Steps:
        1. If the current node marks the end of a word, classify it as an anagram
           or a sub-anagram based on the prefix length.
        2. Traverse child nodes if their letters are available in the remaining frequency.
        3. Backtrack after exploring a child to restore the frequency state.

        Args:
            current (TrieNode): The current node in the Trie.
            freq (Dict[str, int]): Frequency of remaining letters.
            prefix (str): The current prefix string being formed.
            anagrams (Set[str]): A set to store found anagrams.
            sub_anagrams (Set[str]): A set to store found sub-anagrams.
            word_length (int): The length of the input word.
        """
        # Check if the current node ends a word
        if current.is_end_of_word:
            for found_word in current.words:
                if len(prefix) == word_length:
                    anagrams.add(found_word)  # Exact match -> anagram
                else:
                    sub_anagrams.add(found_word)  # Subset match -> sub-anagram

        # Traverse child nodes
        for letter, child in current.children.items():
            if freq.get(letter, 0) > 0:  # Proceed only if the letter is available
                freq[letter] -= 1  # Use the letter
                self._search_anagrams_and_sub_anagrams(
                    current=child,
                    freq=freq,
                    prefix=prefix + letter,
                    anagrams=anagrams,
                    sub_anagrams=sub_anagrams,
                    word_length=word_length
                )
                freq[letter] += 1  # Backtrack to restore the frequency
