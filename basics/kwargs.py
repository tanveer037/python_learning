from random import shuffle
from sys import prefix


def combine_words(word,**kwargs):
        if 'prefix' in kwargs:
           result = kwargs['prefix'] + word
        elif 'suffix' in kwargs:
           result = word + kwargs['suffix']
        else: result = word
        return result
print(combine_words("child", prefix="man"))