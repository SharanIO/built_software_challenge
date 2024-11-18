"""
TrieLetterSolver: Find anagrams and sub-anagrams of a given word using a Trie.

This program builds a Trie from a word list and uses recursive traversal to find all valid words
(anagrams and sub-anagrams) that can be formed from the input word's letters.

The program uses the following steps:
1. Loads Trie data structure with words from a word list file.
2. Generates all valid combinations of letters from the input word.
3. Generates all valid permutations of each combination.
4. Searches the Trie for valid words and identifies anagrams and sub-anagrams.

Author: Sai Sharan Thirunagari
Date: 11-15-2024
"""

from itertools import permutations, combinations
from collections import Counter
from typing import Set, Tuple
from utils import Trie


class TrieLetterSolver:
    """A class to find anagrams and sub-anagrams using Trie data structure.
    
    The Trie enables efficient word lookups while combinations and permutations
    generate possible subsets and arrangements of the input word.
    """

    def __init__(self, trie: Trie) -> None:
        """Initialize the JumbleSolver by building a Trie from a word list."""
        self.trie = trie

    def _generate_combinations(self, word: str) -> Set[Tuple[str, ...]]:
        """
        Generate all valid subsets of letters from the input word

        Subsets are generated for all lengths from 1 to the length of the word, while ensuring
        the subsets respect the frequency of each letter.
        
        Args:
            word (str): The input word to generate subsets for.

        Returns:
            Set[Tuple[str, ...]]: A set of valid combinations of letters as tuples.
        """

        word_counter: Counter[str] = Counter(word)
        valid_combinations: Set[Tuple[str, ...]] = set()

        for r in range(1, len(word) + 1):
            for combo in combinations(word, r):
                combo_counter: Counter[str] = Counter(combo)
                if all(combo_counter[letter] <= word_counter[letter] for letter in combo):
                    valid_combinations.add(combo)

        return valid_combinations

    def _generate_permutations(self, combo: Tuple[str, ...]) -> Set[str]:
        """
        Generate all valid permutations of the input combination.

        Args:
            combo (Tuple[str, ...]): The input combination of letters.

        Returns:
            Set[str]: A set of valid permutations of the input combination.
        """
        valid_permutations: Set[str] = set()
        for perm in permutations(combo):
            valid_permutations.add(''.join(perm))
        return valid_permutations

    def find_anagrams_and_subanagrams(self, word_input: str) -> Tuple[Set[str], Set[str]]:
        """
        Identify anagrams and sub-anagrams for the given word.
        
        Anagrams are words from the Trie that match the input word in letter count.
        Sub-anagrams are words that can be formed using a subset of the input word's letters.
        
        Args:
            input_word (str): The input word to find anagrams and sub-anagrams for.
            
        Returns:
            Tuple[Set[str], Set[str]]: A tuple containing two sets:
                - A set of anagrams of the input word.
                - A set of sub-anagrams of the input word.
        """

        word_input = word_input.lower()
        all_combinations = self._generate_combinations(word_input)

        anagrams: Set[str] = set()
        sub_anagrams: Set[str] = set()

        for combo in all_combinations:
            for word in self._generate_permutations(combo):
                if len(word) == len(word_input) and self.trie.search(word):
                    anagrams.add(word)
                elif self.trie.search(word):
                    sub_anagrams.add(word)

        return sorted(list(anagrams)), sorted(list(sub_anagrams))
