"""
    Method 4: Find anagrams and subanagrams of a given word using hash map 
    with letter frequency count.
"""

def preprocess_word_list(word_list_file: str) -> dict:
    """
    Preprocess the word list file and create a dictionary mapping sorted letters to words.
    
    Args:
        word_list_file (str): The path to the word list file.
        
    Returns:
        dict: A dictionary mapping sorted letters to words.
    """

    local_word_letter_counts = {}
    with open(word_list_file, 'r', encoding='utf-8') as file:
        for line in file.read().split():
            word = line.lower()
            letter_counts = get_letter_counts(word)
            local_word_letter_counts[word] = letter_counts
    return local_word_letter_counts

def get_letter_counts(word: str) -> dict:
    """
    Count the frequency of each letter in the input word.
    
    Args:
        word (str): The input word.
        
    Returns:
        dict: A dictionary mapping each letter to its frequency in the word.
    """

    letter_counts = {}
    for letter in word:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def find_angrams_and_subanagrams(in_word: str, letter_counts_dict: dict) -> tuple:
    """
    Find anagrams and subanagrams of the input word using the preprocessed word list.
    
    Args:
        input_word (str): The input word.
        word_letter_counts (dict): A dictionary mapping words to their letter counts.
        
    Returns:
        tuple: A tuple containing a list of anagrams and a list of subanagrams.
    """

    input_word = in_word.lower()
    input_letter_counts = get_letter_counts(input_word)

    local_anagrams = []
    local_subanagrams = []
    for word, letter_counts in letter_counts_dict.items():
        if len(word) > len(input_word):
            continue
        is_anagram = True
        for letter, count in letter_counts.items():
            if input_letter_counts.get(letter, 0) < count:
                is_anagram = False
                break
        if is_anagram:
            if len(word) == len(input_word):
                local_anagrams.append(word)
            else:
                local_subanagrams.append(word)
    return local_anagrams, local_subanagrams

if __name__ == '__main__':
    word_letter_counts = preprocess_word_list('data/words_alpha.txt')
    user_input = input('Enter the word: ')
    anagrams, subanagrams = find_angrams_and_subanagrams(user_input, word_letter_counts)
    print(f'Anagrams: {anagrams}')
    print(f'Subanagrams: {subanagrams}')
