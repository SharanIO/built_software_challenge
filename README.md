# Anagram and Sub-Anagram Solver

This repository provides a Python solution for efficiently finding Anagrams and Sub-Anagrams of a given word. Designed with modularity and scalability in mind, this project explores multiple approaches to solving the problem, demonstrating the use of efficient data structures and algorithms.

## Problem Statement

An anagram is formed by rearranging all the letters of a word to create a new valid word, while a sub-anagram uses a subset of the letters. For example:
- Anagrams of "cat": `act`, `tac`
- Sub-anagrams of "cat": `a`, `ac`, `cat`, `t`

Note: All the words present in the words_alpha.txt are considered to be valid English words. Therefore, any possible anagram and sub-anagram must be present in the data.

## Methodology

The naive approach involves generating all combinations and sub-combinations of the input word and validating them against the dataset. However, this method becomes inefficient for words longer than a few characters due to exponential growth:

    -For a 5-letter word, there are 325 permutations.
    -For a 10-letter word, this grows to over 10 million permutations.
    -For a 15-letter word, it exceeds 1 trillion permutations, making validation infeasible.

To improve efficiency, we filter/search the data based on the input word's characteristics: the length of the word and the frequency of letters.

1. **Length of the Word**: 
    - Filter the dataset to include only words that have the same length as the input word. This reduces the number of candidate words significantly.

2. **Frequency of Letters**: 
    - For each word in the filtered dataset, check if it has the same frequency of each letter as the input word or a subset of those letters. This ensures that the candidate words are potential anagrams or sub-anagrams.

This approach avoids generating unnecessary combinations, drastically reducing computational overhead and making the solution scalable even for brute force approach. So let's dive into it.

### 1. **Brute Force Method**

**Description**  
The brute force method identifies anagrams and sub-anagrams of a given word by comparing letter frequencies using Python's `Counter` from the `collections` module. This approach systematically evaluates each word in the dataset to check if it qualifies as an anagram or sub-anagram. The steps include:

1. Convert the input word to lowercase for case-insensitive matching.
2. Compute the frequency of each letter in the input word.
3. Iterate through each word in the dataset:
   - **Anagrams**: Verify if the word has the same length and identical letter frequencies as the input word.
   - **Sub-anagrams**: Check if the word's letter frequencies are a subset of the input word's frequencies.

While this method ensures correctness, it does so by performing exhaustive comparisons.

**Complexity**  
The brute force method has a computational complexity of `O(N*M)`, where:
- `N`: The number of words in the dataset.
- `M`: The average length of the words.

- **Preprocessing**: Computing the letter frequencies for all words and the input word takes `O(N*M)`.
- **Lookup**: Comparing each word involves checking `O(N*M)` letters.

This makes the method manageable for small datasets but inefficient for larger ones.

**Advantages**  
- **Simplicity**: The implementation is straightforward and easy to understand.  
- **Accuracy**: Both anagrams and sub-anagrams are identified reliably without requiring additional preprocessing or advanced data structures.

**Limitations**  
- **Scalability**: Performance degrades for larger datasets, as every word must be evaluated individually.  
- **Memory Usage**: The entire dataset is loaded into memory, which can be challenging for very large datasets.  
- **Performance**: For long input words, frequent letter count comparisons increase the computation time.

As the primary bottleneck lies in repeatedly iterating over all the words and performing letter frequency comparisons for each. This redundancy inspired the need for a more efficient solution—one that could reduce lookup times and avoid repeated computations.

By leveraging hashmaps, we can:
1. **Precompute Frequencies**: Store precomputed letter frequencies for each word in a structured format, enabling faster lookups.
2. **Group Words**: Use hashmaps to group words with identical or compatible letter frequencies, minimizing the number of comparisons.
3. **Optimized Retrieval**: Efficiently retrieve candidate anagrams and sub-anagrams using the hashmap's constant-time access properties.

Hashmaps allow us to shift from a computation-heavy approach to one that relies on structured data, significantly improving performance for larger datasets thus leading to my next approach.

---
### 2. Frequency-Based Hashmap Approach

**Description**  
The **frequency-based hashmap** uses letter frequency counts as keys and groups words with matching counts. It works as follows:
1. Convert the input word to lowercase for case-insensitive matching.
2. Calculate the frequency count of each letter in the input word.
3. Use the frequency count to:
   - Retrieve **anagrams**: Words with the exact same frequency count as the input word.
   - Find **sub-anagrams**: Words with letter frequencies that are subsets of the input word's frequencies.

**Complexity**:
- **Preprocessing**:  
  Creating the hashmap involves calculating the frequency count for each word in the dataset and storing it.  
  Time complexity: `O(N*M)`, where:
  - `N`: Number of words in the dataset.
  - `M`: Average length of the words.

- **Lookup**:  
  - For anagrams: Retrieving anagrams by looking up the frequency key in the hashmap is `O(1)` (constant time).  
  - For sub-anagrams: Checking for sub-anagrams requires iterating through all keys in the hashmap, leading to a complexity of `O(K*M)`, where:
    - `K`: Number of unique keys in the hashmap.

**Advantages**:
- Efficiently handles both anagrams and sub-anagrams.
- Reduces redundant calculations by leveraging precomputed frequency counts.
- Scalable for medium to large datasets.

**Limitations**:
- Sub-anagrams still require iterating through all keys in the hashmap, limiting the efficiency gains compared to anagrams.
- Preprocessing requires calculating the frequency counts for all words in the dataset, which can be time-intensive for very large datasets.
- Increased memory usage due to storing frequency-based hashmaps.

#### A Note on Similar Hashmap Approach based on sorting:
The **sorted hashmap** is a simpler alternative, where the keys are the sorted letters of the words, and the values are lists of words sharing those letters. This approach also:
- Optimizes lookups for **anagrams** by allowing direct retrieval via the sorted input word as a key.
- Requires preprocessing, which involves sorting each key word in the dataset.

---
### 3. Trie-Based Approach: Optimizing Sub-Anagram Lookup

While the frequency-based hashmap approach is efficient for retrieving anagrams, finding sub-anagrams still requires iterating through all the keys in the hashmap. This limitation can be partially addressed using **binary search** on the keys; however, binary search is not an ideal solution due to its inefficiency in this specific context.

To further optimize sub-anagram lookup, a **trie (prefix tree)** is used to organize the dataset. By sorting each word and inserting it into the trie, we can efficiently search for anagrams and sub-anagrams. The trie structure allows for partial matches and reduces the amount of data searched by narrowing down candidates through prefixes.

#### Description
The Trie-based approach works as follows:
1. **Trie Construction**: Each word is sorted alphabetically and inserted into the Trie, with nodes representing individual letters. Words sharing common prefixes share the same branches in the Trie.
2. **Search for Anagrams**:
   - Traverse the Trie using the exact sorted letters of the input word.
   - Anagrams are identified when the length of the current prefix matches the input word.
3. **Search for Sub-Anagrams**:
   - Recursively traverse the Trie, checking if the letter frequencies of the input word can accommodate the current path.
   - Sub-anagrams are found when the prefix represents a valid word that uses a subset of the input word’s letters.

#### Complexity Analysis
- **Preprocessing**:
  - Sorting each word: `O(N*Mlog M)`, where:
    - `N`: Number of words in the dataset.
    - `M`: Average length of the words.
  - Inserting into the Trie: `O(N*M)`.
  - Total preprocessing complexity: `O(N* Mlog M)`.

- **Lookup**:
  - Traversing the Trie is efficient as it prunes unnecessary paths early:
    - For anagrams: `O(M)`, as it directly follows the path of the sorted input word.
    - For sub-anagrams: `O(K*d)`, where:
      - `K`: Number of valid paths in the Trie for the given input word.
      - `d`: Depth of the Trie (bounded by the maximum word length).

#### Advantages
- **Efficient Sub-Anagram Search**: The Trie structure minimizes unnecessary checks by limiting the search space to relevant prefixes.
- **Reduced Redundancy**: Words with common prefixes share branches, reducing storage overhead for similar words.
- **Scalable for Anagram Queries**: Lookups for anagrams are direct and efficient, leveraging the sorted structure.

#### Disadvantages
- **High Memory Usage**: Storing the entire dataset in a Trie, especially for large vocabularies, can consume significant memory.
- **Preprocessing Time**: Sorting and constructing the Trie can be time-intensive for very large datasets.
- **Complex Implementation**: The recursive nature of sub-anagram searches adds complexity to the implementation.

---






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
