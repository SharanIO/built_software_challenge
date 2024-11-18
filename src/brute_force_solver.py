"""
    Brute force solver: Find anagrams and subanagrams of a given word.
    
    This program reads a word list from a file and finds all anagrams and sub-anagrams
    of a given input word by comapring the letters and their counts.
    
    The program uses the following steps:
    1. Read the word list from a file.
    2. Find anagrams by comparing the letter counts of the 
    input word and the words in the list.
    3. Find sub-anagrams by checking if the letter counts of 
    the input word are greater than or equal to the word in the list.
    4. Print the anagrams and sub-anagrams of the input word.
    
    Author: Sai Sharan Thirunagari
    Date: 11-15-2024
"""

from collections import Counter
from typing import List, Tuple


class BruteForceAnagramSolver:
    """A class to solve jumble puzzles by finding anagrams and sub-anagrams.
    
    This class compares the letter counts of a given input word against a wrd list.
    It identifies:
    - Anagrams: Words that have the same letters as the input word.
    - Sub-anagrams: Words that can be formed using a subset of the letters in the input word.
    """

    def __init__(self, word_list: List[str]) -> None:
        """
        Initialize the JumbleSolver with a word list.
        
        Args:
            word_list (List[str]): A list of valid words to compare against.
        """
        self.words = word_list

    @staticmethod
    def _get_letter_count(word: str) -> Counter:
        """
        Count the frequency of each letter in the word.
        
        This method creates a Counter object to store the frequency of each letter in the word.

        Args:
            word (str): The input word to count the letter frequency.

        Returns:
            Counter: A Counter object with the frequency of each letter in the word.
        """
        return Counter(word)

    def find_anagrams_and_subanagrams(self, word_input: str) -> Tuple[List[str], List[str]]:
        """
        Get anagrams and sub-anagrams of the input word.

        Args:
            word_input (str): The input word for which anagrams and sub-anagrams.

        Returns:
            tuple: A tuple containing a list of anagrams and a list of sub-anagrams.
        """
        word_input = word_input.lower()
        input_counter = self._get_letter_count(word_input)


        local_anagrams: List[str] = []
        local_subanagrams: List[str] = []

        for word in self.words:
            word_counter = self._get_letter_count(word)

            # Check if the word is an anagram
            if len(word) == len(word_input):
                if word_counter == input_counter:
                    local_anagrams.append(word)

            # Check if the word is a sub-anagram
            if len(word) < len(word_input):
                if all(word_counter[letter] <= input_counter[letter] for letter in word_counter):
                    local_subanagrams.append(word)

        return local_anagrams, local_subanagrams
