'''method_2 for solving the problem'''


class TrieNode:
    '''TrieNode class'''

    def __init__(self):
        '''Initializes the TrieNode class'''
        self.children = {}
        self.is_end_of_word = False


class Trie:
    '''Trie class'''

    def __init__(self):
        '''Initializes the Trie class'''
        self.root = TrieNode()

    def insert(self, word):
        '''Inserts a word into the trie'''
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        '''Searches for a word in the trie'''
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        '''Searches for a prefix in the trie'''
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


class JumbleSolver:
    '''JumbleSolver class'''

    def __init__(self):
        '''Reading the word list'''
        self.trie = Trie()
        with open('data/words_alpha.txt', 'r', encoding='utf-8') as file:
            for word in file.read().split():
                self.trie.insert(word)

    def permute(self, word):
        '''Permute the word'''
        if len(word) == 1:
            return [word]
        permutations = []
        for index, char in enumerate(word):
            for perm in self.permute(word[:index] + word[index + 1:]):
                permutations.append(char + perm)
        return permutations

    def get_anagrams_and_subanagrams(self, word_input):
        '''Getting anagrams and subanagrams'''
        anagram_list = []
        subanagram_list = []
        for perm in self.permute(word_input):
            if self.trie.search(perm):
                anagram_list.append(perm)
            if self.trie.starts_with(perm):
                subanagram_list.append(perm)
        return anagram_list, subanagram_list


if __name__ == '__main__':
    js = JumbleSolver()
    input_word = input('Enter the word: ')
    anagrams, subanagrams = js.get_anagrams_and_subanagrams(input_word)
    print(f'Anagrams: {anagrams}')
    print(f'Subanagrams: {subanagrams}')
