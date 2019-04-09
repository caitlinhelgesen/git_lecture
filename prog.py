import random


def num_vowels(word):
    letters = 0
    for i in word:
        if i in [a,e,i,o,u]:
            letters += 1
    return letters
