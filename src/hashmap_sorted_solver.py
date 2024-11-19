"""
    HashMapSolver: Find anagrams and subanagrams of a given word using hash map

    This program reads a word list from a file, creates a hashmap of sorted letters to words,
    and then finds all anagrams and subanagrams of a given word using the hashmap.

    The program uses the following steps:
    1. Create a hash map of words from the word list file.
    2. Sort the input word and find all anagrams of the input word from the hash map.
    3. Generate all possible combinations of the input word and find all subanagrams.
    4. Print the anagrams and subanagrams of the input word.

    Author: Sai Sharan Thirunagari
    Date: 11-15-2024

"""

from typing import List, Tuple, Dict, Set


class HashMapSolver:
    """
    A class to find anagrams and sub-anagrams of a given word using a hash map approach.

    This class uses:
    - A hash map to store sorted letters as keys and their corresponding words as values.
    - A method to sort strings using insertion sort.
    - A method to generate all possible combinations (subsets) of a string.
    """

    def __init__(self, words_map: List[str]) -> None:
        """
        Initialize the solver by creating a hash map from the given word list.

        Args:
            words_data (List[str]): A list of words to populate the hash map.
        """
        self.word_map: Dict[str, List[str]] = words_map

    def _sort_string(self, word: str) -> str:
        """
        Sort the characters in a string using insertion sort and return the sorted string.

        Args:
            word (str): The input string to be sorted.

        Returns:
            str: A new string with characters sorted in ascending order.
        """
        chars = list(word)
        n = len(chars)
        for i in range(1, n):
            key = chars[i]
            j = i - 1
            while j >= 0 and key < chars[j]:
                chars[j + 1] = chars[j]
                j -= 1
            chars[j + 1] = key
        return ''.join(chars)

    def _get_combinations(self, letters: str) -> List[str]:
        """
        Generate all non-empty combinations (subsets) of the input letters.

        This method iteratively generates subsets by using bitwise operations
        to include or exclude letters.

        Args:
            letters (str): Input string of letters.

        Returns:
            List[str]: A list of all non-empty combinations of the letters.
        """
        combinations = []
        n = len(letters)
        total_combinations = 2 ** n
        for i in range(1, total_combinations):
            combo = ''
            for j in range(n):
                if i & (1 << j):
                    combo += letters[j]
            combinations.append(combo)
        return combinations

    def find_anagrams_and_subanagrams(self, word: str) -> Tuple[Set[str], Set[str]]:
        """
        Identify anagrams and sub-anagrams for a given word using the word hash map.

        Anagrams are words that match the input word's letter count exactly.
        Sub-anagrams are words that use a subset of the input word's letters.

        Args:
            word (str): The input word to find anagrams and sub-anagrams for.

        Returns:
            Tuple[Set[str], Set[str]]: A tuple containing:
                - A set of anagrams of the input word.
                - A set of sub-anagrams of the input word.
        """
        word = word.lower()
        sorted_input_word = self._sort_string(word)
        
        #Get Anagrams
        anagrams: Set[str] = set(self.word_map.get(sorted_input_word, []))
        
        #Get Sub-anagrams
        sub_anagrams: Set[str] = set()

        combos = self._get_combinations(word)

        for combo in combos:
            sorted_combo = self._sort_string(combo)
            if sorted_combo == sorted_input_word:
                continue
            if sorted_combo in self.word_map:
                sub_anagrams.update(self.word_map[sorted_combo])

        return anagrams, sub_anagrams
