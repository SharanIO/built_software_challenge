"""
    Method 5: Find anagrams and sub-anagrams of a given word using a Trie 
    with letter frequency counts.

    This module contains the implementation of the fifth method, which uses 
    a Frequency Trie to efficiently find anagrams and sub-anagrams of a given word.

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
        word = word.lower()
        current: TrieNode = self.root
        anagrams: Set[str] = set()
        sub_anagrams: Set[str] = set()
        freq = self._get_frequency_dict(word)

        self._search_anagrams_and_sub_anagrams(
            current=current,
            freq=freq,
            prefix="",
            anagrams=anagrams,
            sub_anagrams=sub_anagrams,
            word_length=len(word)
        )

        anagrams.discard(word)
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

        Args:
            current (TrieNode): The current node in the Trie.
            freq (Dict[str, int]): The frequency dictionary of remaining letters.
            prefix (str): The current prefix string being formed.
            anagrams (Set[str]): Set to store found anagrams.
            sub_anagrams (Set[str]): Set to store found sub-anagrams.
            word_length (int): The length of the input word.
        """
        if current.is_end_of_word:
            for found_word in current.words:
                if len(prefix) == word_length:
                    anagrams.add(found_word)
                else:
                    sub_anagrams.add(found_word)
        for (letter, count), child in current.children.items():
            if freq.get(letter, 0) >= count:
                # Use the letter
                freq[letter] -= count
                self._search_anagrams_and_sub_anagrams(
                    current=child,
                    freq=freq,
                    prefix=prefix + letter * count,
                    anagrams=anagrams,
                    sub_anagrams=sub_anagrams,
                    word_length=word_length
                )
                # Backtrack
                freq[letter] += count
