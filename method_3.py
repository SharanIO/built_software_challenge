"""
    Method 3: Find anagrams and subanagrams of a given word using hash map

    This program reads a word list from a file, creates a hashmap of sorted letters to words,
    and then finds all anagrams and subanagrams of a given word using the hashmap.

    The program uses the following steps:
    1. Create a hash map of words from the word list file.
    2. Sort the input word and find all anagrams of the input word from the hash map.
    3. Generate all possible combinations of the input word and find all subanagrams.
    4. Print the anagrams and subanagrams of the input word.

    Author: Sai Sharan Thirunagari
    Date: 11-15-2024

"""

from collections import defaultdict

def create_word_hash_map(word_list_file: str) -> dict:
    """
    Create a hash map where each key is a sorted letters of a word,
    and the value is a list of words (anagrams) that match those letters

    Args:
        word_list_file: A string representing the path to the word list file
        
    Returns:
        dict: A dictionary mapping sorted letters to a list of words
    """

    word_map = defaultdict(list)
    with open(word_list_file, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            sorted_word = sort_string(word)
            word_map[sorted_word].append(word)
    return word_map

def sort_string(word: str) -> str:
    """
    Sort the characters in the string word using instertion sort and return the sorted string
    
    Args:
        word (str): The input string to be sorted
        
    Returns:
        str: A new string with characters sorted in ascending order
    """

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
    """
    Generate all non-empty combinations (subsets) of the input letters.
    
    Args:
        letters (str): Input string of letters
        
    Returns:
        list: Alist of all non-empty combinations of the letters.
    """

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
    """
    Get anagrams and subanagrams of a given word using the word hash map.
    
    Args:
        word (str): The input word.
        word_map (dict): Dictionary mapping sorted letters to words.
        
    Returns:
        tuple: A tuple containing two sets:
            - A set of anagrams of the input word.
            - A set of subanagrams of the input word.
    """

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

def main():
    """
    Main function to find anagrams and subanagrams of a given word.
    
    """

    word_hashmap = create_word_hash_map('data/words_alpha.txt')
    query = input('Enter the word: ')
    anagrams, sub_anagram_set = get_anagrams_and_subanagrams(query, word_hashmap)
    print(f'\nAnagrams of "{query}":')
    if anagrams:
        for word in anagrams:
            print(word)
    else:
        print('No anagrams found.')
    print(f'\nSub-anagrams of "{query}":')
    if sub_anagram_set:
        for word in sub_anagram_set:
            print(word)
    else:
        print('No sub-anagrams found.')


if __name__ == '__main__':
    main()
