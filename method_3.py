'''method_3 for solving the problem'''

from collections import defaultdict

def create_word_hash_map(word_list_file: str) -> dict:
    '''Create a hash map of words'''
    word_map = defaultdict(list)
    with open(word_list_file, 'r', encoding='utf-8') as file:
        for word in file.read().split():
            word_map[''.join(sorted(word))].append(word)
    return word_map

def permute(word):
    '''Permute the word'''
    if len(word) == 1:
        return [word]
    perm_list = []
    for index, char in enumerate(word):
        for perm in permute(word[:index] + word[index + 1:]):
            perm_list.append(char + perm)
    return perm_list

def get_anagrams_and_subanagrams(perms: list, word_map: dict) -> tuple:
    '''Get anagrams and subanagrams'''
    local_anagrams = []
    local_subanagrams = []
    for perm in perms:
        local_anagrams.extend(word_map[perm])
        for i in range(1, len(perm)):
            local_subanagrams.extend(word_map[perm[:i]])
    return local_anagrams, local_subanagrams

if __name__ == '__main__':
    word_hash_map = create_word_hash_map('data/words_alpha.txt')
    input_word = input('Enter the word: ')
    permutations = permute(input_word)
    anagrams, subanagrams = get_anagrams_and_subanagrams(permutations, word_hash_map)
    print(f'Anagrams: {anagrams}')
    print(f'Subanagrams: {subanagrams}')
