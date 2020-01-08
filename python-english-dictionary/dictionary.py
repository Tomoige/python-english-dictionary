import json, sys
import difflib
from difflib import get_close_matches
from difflib import SequenceMatcher

with open('dictionary.json') as json_data:
    data = json.load(json_data)

def define(word):
    close_match = (get_close_matches(word, data.keys()))
    close_match = close_match[0]
    match_ratio = SequenceMatcher(None, word, close_match).ratio()

    if word in data:
        return data[word]

    elif match_ratio > .7:
        return did_you_mean(close_match)

    else:
        return 'Word not found.'

def did_you_mean(close_match):
    a = input(f'Word not found did you mean \'{close_match}\'? (Y/N) ').lower()
    if a == 'y':
        return data[close_match]
    elif a == 'n':
        return 'Word not found.'
    else:
        return 'Not a valid option.'

word = input("Enter word: ").lower()

print(define(word))
