import random
import json


def num_vowels(word): #creates a function
    vowels = ["a", "e", "i", "o", "u"]
    letters = 0 #initializes counter at zero
    for i in word: #for loop to iterate through word
        if i in vowels: #find vowels
            letters += 1 #count letters
    return letters #return

print(num_vowels("hello"))
