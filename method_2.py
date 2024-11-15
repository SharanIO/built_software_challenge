"""
Method 2: Find anagrams and sub-anagrams of a given word using a Trie.

This program builds a Trie from a word list and uses recursive traversal to find all valid words
(anagrams and sub-anagrams) that can be formed from the input word's letters.

The program uses the following steps:
1. Create a Trie from a word list file.
2. Use recursive traversal to find all valid words using the input letters.
3. Separate anagrams and sub-anagrams based on word length.
4. Print the anagrams and sub-anagrams of the input word.

Author: Sai Sharan Thirunagari
Date: 11-15-2024
"""

from collections import Counter
from typing import Dict, Set, Tuple


class TrieNode:
    """A node in the Trie structure."""

    def __init__(self) -> None:
        """Initialize the TrieNode with children and is_end_of_word attributes."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class Trie:
    """A Trie data structure to store words."""

    def __init__(self) -> None:
        """Initialize the Trie with a root node."""
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word (str): The word to be inserted into the Trie.
        """
        current: TrieNode = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True


class JumbleSolver:
    """A class to solve jumble puzzles by finding anagrams and sub-anagrams."""

    def __init__(self) -> None:
        """Initialize the JumbleSolver by building a Trie from a word list."""
        self.trie: Trie = Trie()
        try:
            with open('data/words_alpha.txt', 'r', encoding='utf-8') as file:
                for word in file.read().split():
                    self.trie.insert(word.lower())
        except FileNotFoundError:
            print("Word list file 'data/words_alpha.txt' not found.")
            exit(1)

    def find_anagrams_and_subanagrams(self, input_word: str) -> Tuple[Set[str], Set[str]]:
        """
        Find anagrams and sub-anagrams of the input word using recursive Trie traversal.

        Args:
            input_word (str): The input word.

        Returns:
            tuple: A tuple containing two sets:
                - anagrams: Set of anagrams of the input word.
                - sub_anagrams: Set of sub-anagrams of the input word.
        """
        input_word = input_word.lower()
        input_length: int = len(input_word)
        input_letter_counts: Counter[str] = Counter(input_word)
        anagrams: Set[str] = set()
        sub_anagrams: Set[str] = set()
        self._search(
            node=self.trie.root,
            letter_count=input_letter_counts,
            path='',
            input_length=input_length,
            anagrams=anagrams,
            sub_anagrams=sub_anagrams,
        )
        return anagrams, sub_anagrams

    def _search(
        self,
        node: TrieNode,
        letter_count: Counter[str],
        path: str,
        input_length: int,
        anagrams: Set[str],
        sub_anagrams: Set[str],
    ) -> None:
        """
        Recursively search for anagrams and sub-anagrams in the Trie.

        Args:
            node (TrieNode): The current node in the Trie.
            letter_count (Counter[str]): Counter of remaining letters to use.
            path (str): The current word being formed.
            input_length (int): Length of the input word.
            anagrams (Set[str]): Set to store anagrams.
            sub_anagrams (Set[str]): Set to store sub-anagrams.
        """
        if node.is_end_of_word and path:
            if len(path) == input_length:
                anagrams.add(path)
            else:
                sub_anagrams.add(path)
        for letter, child in node.children.items():
            if letter_count.get(letter, 0) > 0:
                # Use the letter
                letter_count[letter] -= 1
                self._search(
                    node=child,
                    letter_count=letter_count,
                    path=path + letter,
                    input_length=input_length,
                    anagrams=anagrams,
                    sub_anagrams=sub_anagrams,
                )
                # Backtrack
                letter_count[letter] += 1


def main() -> None:
    """Main function to execute the JumbleSolver."""
    js = JumbleSolver()
    user_input: str = input('Enter the word: ').strip()
    anagrams, sub_anagrams = js.find_anagrams_and_subanagrams(user_input)
    print(f'\nAnagrams of "{user_input}":')
    if anagrams:
        for word in sorted(anagrams):
            print(word)
    else:
        print("No anagrams found.")

    print(f'\nSub-anagrams of "{user_input}":')
    if sub_anagrams:
        for word in sorted(sub_anagrams):
            print(word)
    else:
        print("No sub-anagrams found.")


if __name__ == '__main__':
    main()
