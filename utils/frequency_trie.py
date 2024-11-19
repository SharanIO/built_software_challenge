"""
FrequencyTrie: A Trie-based data structure for storing words.

This module defines a `FrequencyTrie` and its nodes (`TrieNode`) for efficiently
storing and retrieving words based on their sorted letter frequencies.

Features:
- Insert words into the Trie.
- Organize words by sorted letters for easy retrieval.
- Support additional utilities for processing word frequencies.

Example Usage:
    from utils.frequency_trie import FrequencyTrie

    # Initialize and populate the FrequencyTrie
    trie = FrequencyTrie()
    trie.insert("cat")
    trie.insert("act")
"""

from typing import List, Tuple, Dict


class TrieNode:
    """A node in the Trie structure."""

    def __init__(self) -> None:
        """
        Initialize the TrieNode with attributes for children, words, and end-of-word marking.

        Attributes:
            children (Dict[Tuple[str, int], 'TrieNode']): Child nodes keyed by (character, count).
            words (List[str]): List of words stored at this node.
            is_end_of_word (bool): True if the node marks the end of a valid word.
        """
        self.children: Dict[Tuple[str, int], 'TrieNode'] = {}
        self.words: List[str] = []
        self.is_end_of_word: bool = False


class FrequencyTrie:
    """A Trie-based data structure for storing words by their sorted letter frequencies."""

    def __init__(self) -> None:
        """
        Initialize the FrequencyTrie with a root node.

        Attributes:
            root (TrieNode): The root node of the Trie.
        """
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the FrequencyTrie.

        Steps:
        1. Sort the letters of the word alphabetically.
        2. Traverse or create nodes along the path corresponding to the sorted letters.
        3. Mark the last node as an end-of-word and store the word.

        Args:
            word (str): The word to be inserted into the Trie.
        """
        current: TrieNode = self.root
        for char in sorted(word):  # Sort the word alphabetically
            if char not in current.children:
                current.children[char] = TrieNode()  # Create a new node if the character is missing
            current = current.children[char]  # Move to the child node
        current.is_end_of_word = True  # Mark the node as the end of a word
        current.words.append(word)  # Store the word at this node

    def _get_frequency_dict(self, word: str) -> Dict[str, int]:
        """
        Calculate the frequency of each letter in the given word.

        Steps:
        1. Initialize an empty dictionary.
        2. Iterate through the characters of the word and update their counts.

        Args:
            word (str): The word to process.

        Returns:
            Dict[str, int]: A dictionary mapping each letter to its frequency in the word.
        """
        freq_dict: Dict[str, int] = {}
        for char in word:
            freq_dict[char] = freq_dict.get(char, 0) + 1  # Increment the count for each character
        return freq_dict
