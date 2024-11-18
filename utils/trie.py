class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the trie.
        :param word: The word to insert.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        """
        Check if a word exists in the trie.
        :param word: The word to search for.
        :return: True if the word exists, False otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        """
        Check if there are any words in the trie that start with the given prefix.
        :param prefix: The prefix to search for.
        :return: True if the prefix exists, False otherwise.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
