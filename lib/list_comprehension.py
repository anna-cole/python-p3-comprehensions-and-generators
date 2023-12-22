#!/usr/bin/env python3

# To return evens, use the remainder: n % 2 == 0

def return_evens(num_list):
    even_list = [num for num in num_list if num % 2 == 0]
    return even_list

return_evens([0, 1, 3, 5, 7, 8, 9])

# The sentences in sentence_list are represented as strings. To modify each sentence to add an exclamation mark at the end, use a list comprehension to iterate over each sentence in the original list and concatenate an exclamation mark at the end of each sentence. We use the + operator to concatenate.

def make_exclamation(sentence_list):
    exclamation_list = [sentence + '!' for sentence in sentence_list]
    return exclamation_list

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
