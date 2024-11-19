from typing import List, Tuple, Dict

class TrieNode:
    """A node in the Trie structure."""

    def __init__(self) -> None:
        """Initialize the TrieNode with children and is_end_of_word attributes."""
        self.children: Dict[Tuple[str, int], 'TrieNode'] = {}
        self.words: List[str] = []
        self.is_end_of_word: bool = False


class FrequencyTrie:
    """A Trie data structure to store words."""

    def __init__(self) -> None:
        """Initialize the Trie with a root node."""
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Frequency Trie.

        Args:
            word (str): The word to be inserted into the Trie.
        """

        current: TrieNode = self.root
        for char in sorted(word):
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        current.words.append(word)

    def _get_frequency_dict(self, word: str) -> Dict[str, int]:
        """
        Return a dictionary of letter frequencies in the given word.

        Args:
            word (str): The word to process

        Returns:
            Dict[str, int]: A dictionary mapping letters to their frequencies.
        """
        freq_dict: Dict[str, int] = {}
        for char in word:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        return freq_dict
