"""
Anagram Solver: A script to find anagrams and sub-anagrams of a given word.

This script supports multiple methods for solving anagrams and sub-anagrams:
- brute_force: Uses a brute-force approach to find anagrams and sub-anagrams.
- trie: Uses a Trie data structure to find anagrams and sub-anagrams.
- trie_frequency: Uses a FrequencyTrie data structure to find anagrams and sub-anagrams.
- hashmap_sorted: Uses a hash map with sorted letters as keys.
- hashmap_frequency: Uses a hash map with letter frequency counts.

Command-line Arguments:
- word: The word for which to find anagrams and sub-anagrams.
- method: The solving method to use (default: brute_force).
- word-list: Path to the word list file (default: "data/words_alpha.txt").

Example Usage:
    python main.py "cat" --method hashmap_frequency --word-list data/words_alpha.txt
"""

import argparse
from typing import List
from utils.data_loader import load_word_list
from utils.data_manager import DataManager
from src.brute_force_solver import BruteForceAnagramSolver
from src.trie_letters_solver import TrieLetterSolver
from src.trie_frequency_solver import TrieFrequencySolver
from src.hashmap_sorted_solver import HashMapSolver
from src.hashmap_frequency_solver import HashMapFrequencySolver


def main() -> None:
    """
    Main function to parse command-line arguments, initialize the selected solver,
    and find anagrams and sub-anagrams for the input word.

    Returns:
        None
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Find anagrams and sub-anagrams.")
    parser.add_argument("word", help="The word to analyze")
    parser.add_argument(
        "--method",
        choices=["brute_force", "trie", "trie_frequency", "hashmap_sorted", "hashmap_frequency"],
        default="brute_force",
        help="Method to use",
    )
    parser.add_argument(
        "--word-list",
        default="data/words_alpha.txt",
        help="Path to the word list file",
    )
    args = parser.parse_args()

    # Load the word list
    try:
        word_list: List[str] = load_word_list(args.word_list)
    except FileNotFoundError:
        print(f"Error: Word list file not found at {args.word_list}.")
        return

    # Define paths for serialized data
    trie_save_path: str = "data/trie_data.pkl"
    hash_map_save_path: str = "data/hash_map_data.pkl"
    frequency_trie_save_path: str = "data/frequency_trie_data.pkl"
    frequency_hash_map_save_path: str = "data/frequency_hash_map_data.pkl"

    # Select method and solve
    if args.method == "brute_force":
        solver = BruteForceAnagramSolver(word_list)
        anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(args.word)

    elif args.method == "trie":
        # Load or create Trie
        if DataManager.is_data_saved(trie_save_path):
            trie = DataManager.load_data(trie_save_path)
        else:
            trie = DataManager.create_trie(word_list)
            DataManager.save_data(trie, trie_save_path)
        solver = TrieLetterSolver(trie)
        anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(args.word)

    elif args.method == "trie_frequency":
        # Load or create FrequencyTrie
        if DataManager.is_data_saved(frequency_trie_save_path):
            frequency_trie = DataManager.load_data(frequency_trie_save_path)
        else:
            frequency_trie = DataManager.create_frequency_trie(word_list)
            DataManager.save_data(frequency_trie, frequency_trie_save_path)
        solver = TrieFrequencySolver(frequency_trie)
        anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(args.word)

    elif args.method == "hashmap_sorted":
        # Load or create Hash Map
        if DataManager.is_data_saved(hash_map_save_path):
            hash_map = DataManager.load_data(hash_map_save_path)
        else:
            hash_map = DataManager.create_hash_map(word_list)
            DataManager.save_data(hash_map, hash_map_save_path)
        solver = HashMapSolver(hash_map)
        anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(args.word)

    elif args.method == "hashmap_frequency":
        # Load or create Frequency Hash Map
        if DataManager.is_data_saved(frequency_hash_map_save_path):
            frequency_hash_map = DataManager.load_data(frequency_hash_map_save_path)
        else:
            frequency_hash_map = DataManager.create_hash_map_with_frequencies(word_list)
            DataManager.save_data(frequency_hash_map, frequency_hash_map_save_path)
        solver = HashMapFrequencySolver(frequency_hash_map)
        anagrams, sub_anagrams = solver.find_anagrams_and_sub_anagrams(args.word)

    else:
        raise ValueError(f"Unsupported method: {args.method}")

    # Output results
    print(f"Anagrams of '{args.word}': {', '.join(anagrams) if anagrams else 'None'}")
    print(f"Sub-anagrams of '{args.word}': {', '.join(sub_anagrams) if sub_anagrams else 'None'}")


if __name__ == "__main__":
    main()
