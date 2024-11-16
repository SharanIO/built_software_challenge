"""
    This module contains the implementation of the fifth method.
"""

from typing import List, Tuple, Dict


class TrieNode:
    """A node in the Trie structure."""

    def __init__(self) -> None:
        """Initialize the TrieNode with children and is_end_of_word attributes."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.words: List[str] = []
        self.is_end_of_word: bool = False


class FrequencyTrie:
    """A Trie data structure to store words."""

    def __init__(self) -> None:
        """Initialize the Trie with a root node."""
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        freq = self._get_frequency_dict(word)
        freq_items = tuple(sorted(freq.items()))
        current: TrieNode = self.root
        for char, count in freq_items:
            key = (char, count)
            if key not in current.children:
                current.children[key] = TrieNode()
            current = current.children[key]
        current.is_end_of_word = True
        current.words.append(word)

    def _get_frequency_dict(self, word: str) -> Dict[str, int]:
        freq_dict: Dict[str, int] = {}
        for char in word:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        return freq_dict

    def find_anagrams_and_sub_anagrams(self, word: str) -> Tuple[List[str], List[str]]:
        word = word.lower()
        current: TrieNode = self.root
        anagram = set()
        sub_anagram = set()
        freq = self._get_frequency_dict(word)
        self._search_anagrams_and_sub_anagrams(
            current, freq, "", anagram, sub_anagram, word_length=len(word))

        anagram.discard(word)
        sub_anagram.discard(word)
        return list(anagram), list(sub_anagram)

    def _search_anagrams_and_sub_anagrams(self, current: TrieNode, freq: Dict[str, int], prefix: str, anagram: set, sub_anagram: set, word_length: int) -> None:
        if current.is_end_of_word:
            for found_word in current.words:
                if len(prefix) == word_length:
                    anagram.add(found_word)
                else:
                    sub_anagram.add(found_word)
        for (letter, count), child in current.children.items():
            if freq.get(letter, 0) >= count:
                freq[letter] -= count
                self._search_anagrams_and_sub_anagrams(
                    child, freq, prefix + letter * count, anagram, sub_anagram, word_length)
                freq[letter] += count


def main():
    """
    Main function to find anagrams and sub-anagrams of a given word.

    """

    trie = FrequencyTrie()
    try:
        with open('data/words_alpha.txt', 'r', encoding='utf-8') as file:
            for word in file.read().split():
                trie.insert(word)
    except FileNotFoundError:
        print("Word list file 'data/words_alpha.txt' not found.")
        exit(1)

    query = input('Enter the word: ').strip().lower()
    anagrams, subanagrams = trie.find_anagrams_and_sub_anagrams(query)
    print(f'\nAnagrams of "{query}":')
    if anagrams:
        for word in anagrams:
            print(word)
    else:
        print('No anagrams found.')
    print(f'\nSub-anagrams of "{query}":')
    if subanagrams:
        for word in subanagrams:
            print(word)
    else:
        print('No sub-anagrams found.')


if __name__ == '__main__':
    main()
