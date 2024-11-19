"""
Data Manager: Utility for handling serialized data structures and creating Tries and hash maps.

This module provides functionality for:
- Saving and loading serialized data (e.g., Tries, hash maps).
- Checking the existence of serialized files.
- Creating Tries, frequency-based Tries, and hash maps for efficient anagram and sub-anagram solving.

Example Usage:
    from utils.data_manager import DataManager

    # Save data
    DataManager.save_data(my_data_structure, "data/my_data.pkl")

    # Load data
    loaded_data = DataManager.load_data("data/my_data.pkl")

    # Create a Trie
    trie = DataManager.create_trie(["cat", "dog", "bat"])
"""

import os
import pickle
from collections import defaultdict
from typing import Any, List, Dict
from utils.trie import Trie
from utils.frequency_trie import FrequencyTrie


class DataManager:
    """
    A utility class to handle saving and loading of serialized data structures,
    and creation of Tries and hash maps for solving anagrams and sub-anagrams.
    """

    @staticmethod
    def save_data(data: Any, file_path: str) -> None:
        """
        Save a data structure to a file using serialization.

        Args:
            data (Any): The data structure to serialize and save.
            file_path (str): The file path where the data will be saved.

        Returns:
            None
        """
        with open(file_path, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def load_data(file_path: str) -> Any:
        """
        Load a data structure from a serialized file.

        Args:
            file_path (str): The file path from which the data will be loaded.

        Returns:
            Any: The deserialized data structure.
        """
        with open(file_path, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def is_data_saved(file_path: str) -> bool:
        """
        Check if a serialized data file exists.

        Args:
            file_path (str): The file path to check.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.exists(file_path)

    @staticmethod
    def create_trie(words_data: List[str]) -> Trie:
        """
        Create a Trie from a list of words.

        Steps:
        1. Initialize a Trie instance.
        2. Insert each word from the list into the Trie.

        Args:
            words_data (List[str]): List of words to populate the Trie.

        Returns:
            Trie: A populated Trie.
        """
        trie = Trie()
        for word in words_data:
            trie.insert(word)  # Insert each word into the Trie.
        return trie

    @staticmethod
    def create_hash_map(words_data: List[str]) -> Dict[str, List[str]]:
        """
        Create a hash map with sorted letters as keys.

        Steps:
        1. Initialize a default dictionary to group words by sorted letters.
        2. For each word:
            - Sort its letters alphabetically.
            - Use the sorted letters as the key and append the word to the corresponding list.

        Args:
            words_data (List[str]): List of words to populate the hash map.

        Returns:
            Dict[str, List[str]]: A dictionary mapping sorted letters to corresponding words.
        """
        hash_map = defaultdict(list)
        for word in words_data:
            sorted_word = ''.join(sorted(word))  # Sort the letters in the word.
            hash_map[sorted_word].append(word)  # Group the word under the sorted key.
        return hash_map

    @staticmethod
    def create_frequency_trie(words_data: List[str]) -> FrequencyTrie:
        """
        Create a FrequencyTrie from a list of words.

        Steps:
        1. Initialize a FrequencyTrie instance.
        2. Insert each word from the list into the FrequencyTrie.

        Args:
            words_data (List[str]): List of words to populate the FrequencyTrie.

        Returns:
            FrequencyTrie: A populated FrequencyTrie.
        """
        trie = FrequencyTrie()
        for word in words_data:
            trie.insert(word)  # Insert each word into the FrequencyTrie.
        return trie

    @staticmethod
    def create_hash_map_with_frequencies(words_data: List[str]) -> Dict[str, List[str]]:
        """
        Create a hash map of words grouped by letter frequencies.

        Steps:
        1. Initialize a default dictionary to group words by their letter frequency counts.
        2. For each word:
            - Convert it to lowercase.
            - Calculate its letter frequencies.
            - Use the letter frequencies (as a sorted tuple) as the key and group words.

        Args:
            words_data (List[str]): List of words to populate the hash map.

        Returns:
            Dict[str, List[str]]: A dictionary mapping letter frequency counts to corresponding words.
        """
        hash_map = defaultdict(list)
        for word in words_data:
            word = word.lower()  # Ensure case insensitivity.
            letter_counts = DataManager._get_letter_counts(word)  # Get letter frequencies.
            letter_counts_tuple = tuple(sorted(letter_counts.items()))  # Convert to sorted tuple for consistent keys.
            hash_map[letter_counts_tuple].append(word)  # Group the word under the frequency-based key.
        return hash_map

    @staticmethod
    def _get_letter_counts(word: str) -> Dict[str, int]:
        """
        Count the frequency of each letter in the input word.

        Steps:
        1. Initialize a dictionary to store letter frequencies.
        2. Iterate through each letter in the word and update its count.

        Args:
            word (str): The input word.

        Returns:
            Dict[str, int]: A dictionary mapping each letter to its frequency in the word.
        """
        letter_counts = defaultdict(int)
        for letter in word:
            letter_counts[letter] += 1  # Increment count for the current letter.
        return dict(letter_counts)  # Convert defaultdict to a standard dictionary.
