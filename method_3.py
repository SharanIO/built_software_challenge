'''method_3 for solving the problem'''

from collections import defaultdict

def create_word_hash_map(word_list_file: str) -> dict:
    '''Create a hash map of words'''
    word_map = defaultdict(list)
    with open(word_list_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            sorted_word = sort_string(word)
            word_map[sorted_word].append(word)
    return word_map

def sort_string(word: str) -> str:
    '''Sort the string'''
    chars = list(word)
    n = len(chars)
    for i in range(1,n):
        key = chars[i]
        j = i - 1
        while j >= 0 and key < chars[j]:
            chars[j + 1] = chars[j]
            j -= 1
        chars[j + 1] = key
    return ''.join(chars)

def get_combinations(letters: str) -> list:
    '''Generate all possible combinations of the letters'''
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


def get_anagrams_and_subanagrams(word: str, word_map: dict) -> tuple:
    '''Get anagrams and subanagrams'''
    word = word.lower()
    sorted_input_word = sort_string(word)
    local_anagram_set = set(word_map.get(sorted_input_word, []))
    sub_anagrams = set()

    combos = get_combinations(word)
    process_combos = set()
    for combo in combos:
        sorted_combo = sort_string(combo)
        if sorted_combo in process_combos:
            continue
        process_combos.add(sorted_combo)
        if sorted_combo == sorted_input_word:
            continue
        if sorted_combo in word_map:
            sub_anagrams.update(word_map[sorted_combo])
    return local_anagram_set, sub_anagrams

if __name__ == '__main__':
    word_hash_map = create_word_hash_map('data/words_alpha.txt')
    input_word = input('Enter the word: ')
    anagram_set, subanagrams = get_anagrams_and_subanagrams(input_word, word_hash_map)
    print(f'Anagrams: {anagram_set}')
    print(f'Subanagrams: {subanagrams}')
