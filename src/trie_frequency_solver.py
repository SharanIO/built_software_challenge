"""
Trie Frequency Solver: Find anagrams and sub-anagrams of a given word using a Trie 
with letter frequency counts.

This module contains the implementation of the fifth method, which uses 
a Frequency Trie to efficiently find anagrams and sub-anagrams of a given word.

The TrieFrequencySolver class extends the FrequencyTrie class and implements
the find_anagrams_and_subanagrams method to search for anagrams and sub-anagrams
of a given word using the Trie data structure.

The program uses following steps:
1. Initialize the Trie with a root node.
2. Search the Trie for anagrams and sub-anagrams of the input word by recursively searching the Trie.
3. Return the found anagrams and sub-anagrams.

Author: Sai Sharan Thirunagari
Date: 11-15-2024

"""

from typing import List, Tuple, Dict, Set
from utils.frequency_trie import TrieNode, FrequencyTrie


class TrieFrequencySolver(FrequencyTrie):
    """A Trie data structure to store words."""

    def __init__(self, frequency_trie: FrequencyTrie) -> None:
        """Initialize the Trie with a root node."""
        super().__init__()
        self.root = frequency_trie.root

    def find_anagrams_and_subanagrams(self, word: str) -> Tuple[List[str], List[str]]:
        """
        Find all anagrams and sub-anagrams of the given word.

        Args:
            word (str): The input word to find anagrams and sub-anagrams.

        Returns:
            Tuple[List[str], List[str]]: A tuple containing two lists:
                - A list of anagrams of the input word.
                - A list of sub-anagrams of the input word.
        """
        # Ensure the word is in lowercase for uniform comparison
        word = word.lower()
        
        # Start from the root of the Trie
        current: TrieNode = self.root

        # Sets to store unique anagrams and sub-anagrams
        anagrams: Set[str] = set()
        sub_anagrams: Set[str] = set()

        # Generate a frequency dictionary for the input word
        freq = self._get_frequency_dict(word)

        # Recursively search for anagrams and sub-anagrams in the Trie
        self._search_anagrams_and_sub_anagrams(
            current=current,
            freq=freq,
            prefix="",
            anagrams=anagrams,
            sub_anagrams=sub_anagrams,
            word_length=len(word)
        )

        # Remove the original word from the results if it's present
        anagrams.discard(word)
        sub_anagrams.discard(word)

        # Return results as lists
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

        Args:
            current (TrieNode): The current node in the Trie.
            freq (Dict[str, int]): The frequency dictionary of remaining letters.
            prefix (str): The current prefix string being formed.
            anagrams (Set[str]): Set to store found anagrams.
            sub_anagrams (Set[str]): Set to store found sub-anagrams.
            word_length (int): The length of the input word.
        """
        # If this node marks the end of a word, check if it’s an anagram or sub-anagram
        if current.is_end_of_word:
            for found_word in current.words:
                if len(prefix) == word_length:
                    # If the length of the prefix matches the input word, it's an anagram
                    anagrams.add(found_word)
                else:
                    # Otherwise, it's a sub-anagram
                    sub_anagrams.add(found_word)
        for letter, child in current.children.items():
            if freq.get(letter, 0) > 0:
                # Use the letter
                freq[letter] -= 1
                self._search_anagrams_and_sub_anagrams(
                    current=child,
                    freq=freq,
                    prefix=prefix + letter,
                    anagrams=anagrams,
                    sub_anagrams=sub_anagrams,
                    word_length=word_length
                )
                # Backtrack
                freq[letter] += 1
