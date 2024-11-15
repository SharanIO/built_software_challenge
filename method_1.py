'''method_1 for solving the problem'''


class JumbleSolver:
    '''JumbleSolver class'''

    def __init__(self):
        '''Reading the word list'''
        with open('data/words_alpha.txt', 'r', encoding='utf-8') as file:
            self.words = file.read().split()

    def get_anagrams_and_subanagrams(self, word_input):
        '''Getting anagrams and subanagrams'''
        local_anagrams = []
        local_subanagrams = []
        for word in self.words:
            if len(word) == len(word_input) and all(char in set(word_input) for char in word):
                local_anagrams.append(word)
            if len(word) < len(word_input) and all(char in set(word_input) for char in word):
                local_subanagrams.append(word)
        return local_anagrams, local_subanagrams


if __name__ == '__main__':
    js = JumbleSolver()
    input_word = input('Enter the word: ')
    anagrams, subanagrams = js.get_anagrams_and_subanagrams(input_word)
    print(f'Anagrams: {anagrams}')
    print(f'Subanagrams: {subanagrams}')
