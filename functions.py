# functions.py

import string

# 1. Returns a new list with unique elements (keeps first appearance)
def get_unique_list_f(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


# 2. Counts uppercase and lowercase letters in a string
def count_case_f(string):   
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# 3. Removes punctuation marks from a sentence
def remove_punctuation_f(sentence):
    return ''.join(char for char in sentence if char not in string.punctuation)

# 4. Counts the number of words in a given sentence after removing punctuation
def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    return len(words)
