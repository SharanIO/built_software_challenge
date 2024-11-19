"""
Anagram Solver: A script to find anagrams and sub-anagrams of a given word or words.

This script supports multiple methods for solving anagrams and sub-anagrams:
- brute_force: Uses a brute-force approach to find anagrams and sub-anagrams.
- trie_frequency: Uses a FrequencyTrie data structure to find anagrams and sub-anagrams.
- hashmap_sorted: Uses a hash map with sorted letters as keys.
- hashmap_frequency: Uses a hash map with letter frequency counts.

Command-line Arguments:
- word(s): The word(s) for which to find anagrams and sub-anagrams.
- method: The solving method to use (default: brute_force).
- word-list: Path to the word list file (default: "data/words_alpha.txt").

Example Usage:
    python main.py "cat bat" --method hashmap_frequency --word-list data/words_alpha.txt
"""

import argparse
from typing import List
from utils.data_loader import load_word_list
from utils.data_manager import DataManager
from utils.input_validator import validate_input_word
from src.brute_force_solver import BruteForceAnagramSolver
from src.trie_frequency_solver import TrieFrequencySolver
from src.hashmap_sorted_solver import HashMapSolver
from src.hashmap_frequency_solver import HashMapFrequencySolver


def main() -> None:
    """
    Main function to parse command-line arguments, initialize the selected solver,
    and find anagrams and sub-anagrams for the input word(s).

    Returns:
        None
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Find anagrams and sub-anagrams.")
    parser.add_argument("words", help="The word(s) to analyze, separated by spaces")
    parser.add_argument(
        "--method",
        choices=["brute_force", "trie_frequency", "hashmap_sorted", "hashmap_frequency"],
        default="brute_force",
        help="Method to use for solving",
    )
    parser.add_argument(
        "--word-list",
        default="data/words_alpha.txt",
        help="Path to the word list file",
    )
    args = parser.parse_args()

    # Split and validate input words
    input_words: List[str] = args.words.split()
    sanitized_words: List[str] = []
    for word in input_words:
        try:
            sanitized_word = validate_input_word(word)
            sanitized_words.append(sanitized_word)
        except ValueError as e:
            print(f"Error with input word '{word}': {e}")
            return

    # Load the word list
    try:
        word_list: List[str] = load_word_list(args.word_list)
    except FileNotFoundError:
        print(f"Error: Word list file not found at {args.word_list}.")
        return

    if not word_list:
        print("Error: Word list is empty. Please provide a valid dataset.")
        return

    # Paths for serialized data
    hash_map_save_path: str = "data/hash_map_data.pkl"
    frequency_trie_save_path: str = "data/frequency_trie_data.pkl"
    frequency_hash_map_save_path: str = "data/frequency_hash_map_data.pkl"

    # Process each sanitized word
    for word in sanitized_words:
        try:
            if args.method == "brute_force":
                solver = BruteForceAnagramSolver(word_list)
                anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(word)

            elif args.method == "trie_frequency":
                if DataManager.is_data_saved(frequency_trie_save_path):
                    frequency_trie = DataManager.load_data(frequency_trie_save_path)
                else:
                    frequency_trie = DataManager.create_frequency_trie(word_list)
                    DataManager.save_data(frequency_trie, frequency_trie_save_path)
                solver = TrieFrequencySolver(frequency_trie)
                anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(word)

            elif args.method == "hashmap_sorted":
                if DataManager.is_data_saved(hash_map_save_path):
                    hash_map = DataManager.load_data(hash_map_save_path)
                else:
                    hash_map = DataManager.create_hash_map(word_list)
                    DataManager.save_data(hash_map, hash_map_save_path)
                solver = HashMapSolver(hash_map)
                anagrams, sub_anagrams = solver.find_anagrams_and_subanagrams(word)

            elif args.method == "hashmap_frequency":
                if DataManager.is_data_saved(frequency_hash_map_save_path):
                    frequency_hash_map = DataManager.load_data(frequency_hash_map_save_path)
                else:
                    frequency_hash_map = DataManager.create_hash_map_with_frequencies(word_list)
                    DataManager.save_data(frequency_hash_map, frequency_hash_map_save_path)
                solver = HashMapFrequencySolver(frequency_hash_map)
                anagrams, sub_anagrams = solver.find_anagrams_and_sub_anagrams(word)

            else:
                raise ValueError(f"Unsupported method: {args.method}")

            # Output results for the current word in a readable format
            print(f"\nResults for the word: '{word}'")
            print("=" * (len(word) + 20))  # Adds a separator line for better readability

            # Display anagrams
            if anagrams:
                print(f"Anagrams ({len(anagrams)}):")
                print(", ".join(anagrams))
            else:
                print("Anagrams: None")

            # Display sub-anagrams
            if sub_anagrams:
                print(f"Sub-anagrams ({len(sub_anagrams)}):")
                print(", ".join(sub_anagrams))
            else:
                print("Sub-anagrams: None")

            # Add explanatory text
            print("\nNote: All these anagrams and sub-anagrams are from the dataset therefore are considered to be valid English words.")

            print("-" * 40)  # Adds a bottom separator

        except (FileNotFoundError, ValueError, KeyError) as e:
            print(f"Error during solving for word '{word}': {e}")


if __name__ == "__main__":
    main()
