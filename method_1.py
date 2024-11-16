"""
    Method 1: Find anagrams and subanagrams of a given word.
    
    This program reads a word list from a file and finds all anagrams and sub-anagrams
    of a given input word by comapring the letters and their counts.
    
    The program uses the following steps:
    1. Read the word list from a file.
    2. Find anagrams by comparing the letter counts of the input word and the words in the list.
    3. Find sub-anagrams by checking if the letter counts of the input word are greater than or equal to the word in the list.
    4. Print the anagrams and sub-anagrams of the input word.
    
    Author: Sai Sharan Thirunagari
    Date: 11-15-2024
"""

from collections import Counter
from typing import List, Tuple

class JumbleSolver:
    """A class to solve jumble puzzles by finding anagrams and sub-anagrams."""

    def __init__(self):
        """Initialize the JumbleSolver by reading the word list from a file."""
        try:
            with open('data/words_alpha.txt', 'r', encoding='utf-8') as file:
                self.words: List[str] = file.read().split()
        except FileNotFoundError:
            print('Word list file not found. Please make sure the file exists in the data directory.')
            exit(1)

    def get_anagrams_and_subanagrams(self, word_input: str) -> Tuple[List[str], List[str]]:
        """
        Get anagrams and sub-anagrams of the input word.
        
        Args:
            word_input (str): The input word for which anagrams and sub-anagrams.
            
        Returns:
            tuple: A tuple containing a list of anagrams and a list of sub-anagrams.
        """
        word_input = word_input.lower()
        input_counter = Counter(word_input)
        local_anagrams = []
        local_subanagrams = []
        for word in self.words:
            word_counter = Counter(word)
            if len(word) == len(word_input):
                if word_counter == input_counter:
                    local_anagrams.append(word)
            if len(word) < len(word_input):
                if all(word_counter[letter] <= input_counter[letter] for letter in word_counter):
                    local_subanagrams.append(word)
        return local_anagrams, local_subanagrams

def main():
    """
    Main function to find anagrams and sub-anagrams of a given word.
    
    """

    js = JumbleSolver()
    input_word = input('Enter the word: ').strip()
    anagrams, subanagrams = js.get_anagrams_and_subanagrams(input_word)
    print(f'\nAnagrams of "{input_word}":')
    if anagrams:
        for word in anagrams:
            print(word)
    else:
        print('No anagrams found.')
    print(f'\nSub-anagrams of "{input_word}":')
    if subanagrams:
        for word in subanagrams:
            print(word)
    else:
        print('No sub-anagrams found.')

if __name__ == '__main__':
    main()
