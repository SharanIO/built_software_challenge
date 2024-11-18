# built_software_challenge
# Anagram and Sub-Anagram Solver

This Repository is a Python solution for finding **Anaagrams** and **Sub-Anagrams** from a given word. The system is designed with modularity and scalability in mind, to explore multiple solutions the problem can be approached, leading to five distinct solving approaches each aiming to efficiently solve the problem while demonstrating the use of efficient data structure and algorithms.
---

## Problem Statement

An anagram is formed by rearranging all the letters of a word to create a new valid word, while a sub-anagram uses a subset of the letters. For example:
- **Anagrams of "cat"**: `act`, `tac`
- **Sub-anagrams of "cat"**: `a`, `ac`, `cat`, `t`

Note: All the words present in the words_alpha.txt are considered to be valid english words. Therefore, any possible anagram and sub-angram must be present in the data.
---

## Methodology

The problem is approached by generating all possible combinations and sub-combinations of the input word and validating them through the data file to find anagrams and sub-anagrams. However, this method is only efficient for very short words and not suitable for medium to large words.

To improve efficiency, we filter/search the data based on the input word's characteristics: the length of the word and the frequency of letters.

1. **Length of the Word**: 
  - Filter the dataset to include only words that have the same length as the input word. This reduces the number of candidate words significantly.

2. **Frequency of Letters**: 
  - For each word in the filtered dataset, check if it has the same frequency of each letter as the input word or a subset of those letters. This ensures that the candidate words are potential anagrams or sub-anagrams.

### Data Preprocessing

To further improve lookup efficiency, preprocessing the dataset is suggested. This involves organizing the data in a way that makes it faster to search for anagrams and sub-anagrams.

#### Possible Preprocessing Methods

1. **Indexing by Length**:
  - Create an index where words are grouped by their lengths. This allows quick access to words of a specific length.

2. **Letter Frequency Maps**:
  - For each word, create a frequency map (a dictionary where keys are letters and values are their counts).
  - Store these maps in a way that allows quick comparison with the frequency map of the input word.

### Summary

By filtering the dataset based on word length and letter frequency, and by preprocessing the data for efficient lookups, the approach aims to find anagrams and sub-anagrams more efficiently than the brute-force method.

### Example

Let's say the input word is "listen". The steps would be:
1. **Filter by Length**: Only consider words with 6 letters.
2. **Frequency Check**: For each 6-letter word, check if it has the same letter frequencies as "listen" (e.g., 'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1).


## Detailed Approach Analysis

With the foundation laid, let's dive into each approach that led us to seek an efficient solution:

1. **Brute Force Method**:
  - **Description**: This method involves generating all possible combinations and sub-combinations of the input word and validating them through the data file to find anagrams and sub-anagrams. However, this method is only efficient for very short words and not suitable for medium to large words. To improve efficiency, the method filters the dataset based on the input word's characteristics: the length of the word and the frequency of letters. Specifically, it:
    - Converts the input word to lowercase for case-insensitive matching.
    - Gets the letter count of the input word.
    - Iterates through each word in the dataset, getting the letter count for each word.
    - Checks for anagrams by comparing the length and letter frequency count of each word with the input word.
    - Checks for sub-anagrams by ensuring all letter frequencies in the current word are less than or equal to those in the input word.
  - **Complexity**:
    - **Preprocessing**: The preprocessing step involves creating a frequency count for each word in the list. If there are `n` words and the average length of a word is `m`, the complexity is `O(n * m)`.
    - **Lookup**: For each word in the list, the method compares its frequency count with that of the input word. This involves iterating through `n` words and performing a comparison that takes `O(m)` time. Thus, the complexity is `O(n * m)`.
  - **Advantages**: 
    - Simple to implement and understand.
    - Accurately identifies both anagrams and sub-anagrams.
  - **Limitations**: 
    - Inefficient for large datasets due to the need to iterate through all words.
    - No preprocessing optimizations, leading to higher computational costs.
    - Memory usage can be significant for large datasets.

2. **Trie-Based Letter Solver**:
  - **Description**: This approach uses a Trie data structure to store words. Anagrams and sub-anagrams are found by generating valid combinations and permutations of the input word's letters and checking them against the Trie. Specifically, it:
    - Converts the input word to lowercase for case-insensitive matching.
    - Generates all valid combinations of the input word's letters.
    - Generates all unique permutations of each valid combination.
    - Checks each permutation against the Trie to identify anagrams and sub-anagrams.
  - **Complexity**:
    - **Preprocessing**: Building the Trie involves inserting each word from the dataset into the Trie. If there are `n` words and the average length of a word is `m`, the complexity is `O(n * m)`.
    - **Lookup**: Generating valid combinations and permutations involves combinatorial operations. The overall complexity is `O(2^m * m) + O(k! * 2^m)`, where `m` is the length of the input word and `k` is the length of the combinations.
  - **Advantages**: 
    - Efficiently narrows down the search space using common prefixes.
    - Accurately identifies both anagrams and sub-anagrams.
  - **Limitations**: 
    - High computational cost due to exponential and factorial complexity.
    - Memory usage can be significant for large datasets.
    - More complex to implement compared to simpler brute-force approaches.

3. **Trie-Based Frequency Solver**:
  - **Description**: This method extends the Trie structure to include letter frequency counts, allowing direct comparison of letter frequencies to find anagrams and sub-anagrams. Specifically, it:
    - Converts the input word to lowercase for case-insensitive matching.
    - Calculates the frequency count of each letter in the input word.
    - Traverses the Trie, comparing the frequency counts of the nodes with the input word's frequency count.
    - Checks for anagrams by comparing the frequency count of the input word with the frequency counts stored in the Trie nodes.
    - Checks for sub-anagrams by ensuring that the frequency count of each letter in the Trie node is less than or equal to the corresponding count in the input word.
  - **Complexity**:
    - **Preprocessing**: Building the Trie involves inserting each word from the dataset into the Trie with their letter frequency counts. If there are `n` words and the average length of a word is `m`, the complexity is `O(n * m)`.
    - **Lookup**: The traversal and comparison take `O(m)` time for each node visited. The overall complexity is `O(m * v)`, where `m` is the length of the input word and `v` is the number of nodes visited during the traversal.
  - **Advantages**: 
    - Combines the efficiency of Trie traversal with the accuracy of frequency-based matching.
    - Accurately identifies both anagrams and sub-anagrams.
  - **Limitations**: 
    - More complex to implement and may require more memory.
    - Memory usage can be significant for large datasets.

4. **HashMap Sorted Solver**:
  - **Description**: This method uses a hash map where the keys are the sorted letters of words, and the values are lists of words (anagrams) that match those letters. Specifically, it:
    - Converts the input word to lowercase for case-insensitive matching.
    - Sorts the input word.
    - Uses the sorted input word as a key to retrieve the corresponding list of anagrams from the hash map.
  - **Complexity**:
    - **Preprocessing**: Creating the hash map involves sorting each word and inserting it into the hash map. If there are `n` words and the average length of a word is `m`, the complexity is `O(n * m log m)`.
    - **Lookup**: Sorting the input word takes `O(m log m)` time, and retrieving from the hash map takes `O(1)` time. Thus, the overall lookup complexity is `O(m log m)`.
  - **Advantages**: 
    - Fast lookup for anagrams using sorted keys.
    - Simple implementation.
    - Efficient for finding anagrams.
  - **Limitations**: 
    - Not suitable for sub-anagrams.
    - Memory usage can be significant for large datasets.
    - Preprocessing time can be high for very large datasets.

5. **HashMap Frequency Solver**:
  - **Description**: This method uses a hash map where the keys are the letter frequency counts of words, and the values are lists of words (anagrams and sub-anagrams) that match those counts. Specifically, it:
    - Converts the input word to lowercase for case-insensitive matching.
    - Calculates the frequency count of each letter in the input word.
    - Compares the frequency count of the input word with those stored in the hash map.
    - Checks for anagrams by finding words in the hash map that have the same letter frequency count as the input word.
    - Checks for sub-anagrams by finding words in the hash map that have letter frequency counts less than or equal to those in the input word.
  - **Complexity**:
    - **Preprocessing**: Creating the hash map involves calculating the letter frequency count for each word and inserting it into the hash map. If there are `n` words and the average length of a word is `m`, the complexity is `O(n * m)`.
    - **Lookup**: Calculating the frequency count of the input word takes `O(m)` time, and comparing with the hash map takes `O(n)` time in the worst case. Thus, the overall lookup complexity is `O(n * m)`.
  - **Advantages**: 
    - Efficient for both anagrams and sub-anagrams.
    - Simple implementation.
    - Accurate results.
  - **Limitations**: 
    - Memory usage can be significant.
    - Preprocessing time can be high for very large datasets.

### Comparison of Methods

| Method                    | Preprocessing Complexity | Lookup Complexity       | Suitable for Sub-Anagrams | Memory Usage             | Implementation Complexity |
|---------------------------|--------------------------|-------------------------|---------------------------|--------------------------|---------------------------|
| Brute Force               | O(n * m)                 | O(n * m)                | Yes                       | High                     | Simple                    |
| Trie-Based Letter Solver  | O(n * m)                 | O(2^m * m) + O(k! * 2^m)| Yes                       | High                     | Complex                   |
| Trie-Based Frequency Solver| O(n * m)                | O(m * v)                | Yes                       | High                     | Complex                   |
| HashMap Sorted Solver     | O(n * m log m)           | O(m log m)              | No                        | High                     | Simple                    |
| HashMap Frequency Solver  | O(n * m)                 | O(n * m)                | Yes                       | High                     | Simple                    |

### Which Approach is Better?

The choice of the best approach depends on the specific requirements and constraints of the application:

- **For Small Datasets**: The brute force method is simple and effective for small datasets where performance is not a critical concern.
- **For Efficient Anagram Lookup**: The HashMap Sorted Solver is highly efficient for finding anagrams due to its fast lookup time, but it is not suitable for sub-anagrams.
- **For Both Anagrams and Sub-Anagrams**: The Trie-Based Frequency Solver and HashMap Frequency Solver are both efficient for finding anagrams and sub-anagrams. The Trie-Based Frequency Solver offers efficient traversal and accurate results but is more complex to implement. The HashMap Frequency Solver is simpler to implement and provides accurate results but can be memory-intensive.

In summary, the **HashMap Frequency Solver** is generally the best approach for finding both anagrams and sub-anagrams due to its balance of efficiency, simplicity, and accuracy. However, if only anagram lookup is required, the **HashMap Sorted Solver** is the most efficient choice.

## File Structure

The project is organized as follows:
```
built_software_challenge/
├── data/
│   └── words_alpha.txt
├── src/
│   ├── brute_force_anagram_solver.py
│   ├── hashmap_frequency_solver.py
│   ├── hashmap_sorted_solver.py
│   ├── trie_letters_solver.py
│   ├── trie_frequency_solver.py
├── utils/
│   ├── data_loader.py
│   ├── data_manager.py
│   ├── frequency_trie.py
│   ├── trie.py
├── main.py
├── README.md
└── requirements.txt
```

### How to Run

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/built_software_challenge.git
   cd built_software_challenge
   ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Main Script**:
    ```sh
    python src/main.py "your_word" --method hashmap_frequency --word-list data/words_alpha.txt
    ```
  Replace "your_word" with the word you want to find anagrams and sub-anagrams for. You can also specify the method (brute_force, trie_letters, trie_frequency, hashmap_sorted, hashmap_frequency) and the path to the word list file.