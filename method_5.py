"""
    Method 5: Find anagrams and sub-anagrams of a given word using a Trie 
    with letter frequency counts.

    This module contains the implementation of the fifth method, which uses 
    a Frequency Trie to efficiently find anagrams and sub-anagrams of a given word.

"""

from typing import List, Tuple, Dict, Set


class TrieNode:
    """A node in the Trie structure."""

    def __init__(self) -> None:
        """Initialize the TrieNode with children and is_end_of_word attributes."""
        self.children: Dict[Tuple[str, int], 'TrieNode'] = {}
        self.words: List[str] = []
        self.is_end_of_word: bool = False


class FrequencyTrie:
    """A Trie data structure to store words."""

    def __init__(self) -> None:
        """Initialize the Trie with a root node."""
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Frequency Trie.

        Args:
            word (str): The word to be inserted into the Trie.
        """
        freq: Dict[str, int] = self._get_frequency_dict(word)
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
        """
        Return a dictionary of letter frequencies in the given word.

        Args:
            word (str): The word to process

        Returns:
            Dict[str, int]: A dictionary mapping letters to their frequencies.
        """
        freq_dict: Dict[str, int] = {}
        for char in word:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        return freq_dict

    def find_anagrams_and_sub_anagrams(self, word: str) -> Tuple[List[str], List[str]]:
        """
        Find all anagrams and sub-anagrams of the given word.

        Args:
            word (str): The input word to find anagrams and sub-anagrams.

        Returns:
            Tuple[List[str], List[str]]: A tuple containing two lists:
                - A list of anagrams of the input word.
                - A list of sub-anagrams of the input word.
        """
        word = word.lower()
        current: TrieNode = self.root
        anagram: Set[str] = set()
        sub_anagrams: Set[str] = set()
        freq = self._get_frequency_dict(word)
        self._search_anagrams_and_sub_anagrams(
            current, freq, "", anagram, sub_anagrams, word_length=len(word))

        anagram.discard(word)
        sub_anagrams.discard(word)
        return list(anagram), list(sub_anagrams)

    def _search_anagrams_and_sub_anagrams(
        self,
        current: TrieNode,
        freq: Dict[str, int],
        prefix: str,
        anagrams: Set[str],
        sub_anagrams: Set[str],
        word_length: int
    ) -> None:
        """
        Recursively search for anagrams and sub-anagrams in the Trie.

        Args:
            current (TrieNode): The current node in the Trie.
            freq (Dict[str, int]): The frequency dictionary of remaining letters.
            prefix (str): The current prefix string being formed.
            anagrams (Set[str]): Set to store found anagrams.
            sub_anagrams (Set[str]): Set to store found sub-anagrams.
            word_length (int): The length of the input word.
        """
        if current.is_end_of_word:
            for found_word in current.words:
                if len(prefix) == word_length:
                    anagrams.add(found_word)
                else:
                    sub_anagrams.add(found_word)
        for (letter, count), child in current.children.items():
            if freq.get(letter, 0) >= count:
                # Use the letter
                freq[letter] -= count
                self._search_anagrams_and_sub_anagrams(
                    current=child,
                    freq=freq,
                    prefix=prefix + letter * count,
                    anagrams=anagrams,
                    sub_anagrams=sub_anagrams,
                    word_length=word_length
                )
                # Backtrack
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
