import os
import pickle
from collections import defaultdict
from typing import Any, List, Dict
from utils.trie import Trie
from utils.frequency_trie import FrequencyTrie


class DataManager:
    """
    A utility class to handle saving and loading of serialized data structures,
    and creation of Tries and hash maps.
    """

    @staticmethod
    def save_data(data: Any, file_path: str) -> None:
        """
        Save a data structure to a file.

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
        Load a data structure from a file.

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

        Args:
            words_data (List[str]): List of words to populate the Trie.

        Returns:
            Trie: A populated Trie.
        """
        trie = Trie()
        for word in words_data:
            trie.insert(word)
        return trie

    @staticmethod
    def create_hash_map(words_data: List[str]) -> Dict[str, List[str]]:
        """
        Create a hash map from a list of words.

        Args:
            words_data (List[str]): List of words to populate the hash map.

        Returns:
            Dict[str, List[str]]: A dictionary mapping sorted letters to corresponding words.
        """
        hash_map = defaultdict(list)
        for word in words_data:
            sorted_word = ''.join(sorted(word))
            hash_map[sorted_word].append(word)
        return hash_map

    @staticmethod
    def create_frequency_trie(words_data: List[str]) -> FrequencyTrie:
        """
        Create a FrequencyTrie from a list of words.

        Args:
            words_data (List[str]): List of words to populate the FrequencyTrie.

        Returns:
            FrequencyTrie: A populated FrequencyTrie.
        """
        trie = FrequencyTrie()
        for word in words_data:
            trie.insert(word)
        return trie

    @staticmethod
    def create_hash_map_with_frequencies(words_data: List[str]) -> Dict[str, Dict[str, int]]:
        """
        Create a hash map of words with their letter frequencies.

        Args:
            words_data (List[str]): List of words to populate the hash map.

        Returns:
            Dict[str, Dict[str, int]]: A dictionary mapping each word to a dictionary
            of its letter frequencies.
        """
        hash_map = defaultdict(list)
        for word in words_data:
            word = word.lower()
            letter_counts = DataManager._get_letter_counts(word)
            # Convert letter counts to a sorted tuple for consistent hashable keys
            letter_counts_tuple = tuple(sorted(letter_counts.items()))
            hash_map[letter_counts_tuple].append(word)
        return hash_map

    @staticmethod
    def _get_letter_counts(word: str) -> Dict[str, int]:
        """
        Count the frequency of each letter in the input word.

        Args:
            word (str): The input word.

        Returns:
            Dict[str, int]: A dictionary mapping each letter to its frequency in the word.
        """
        letter_counts = defaultdict(int)
        for letter in word:
            letter_counts[letter] += 1
        return dict(letter_counts)
