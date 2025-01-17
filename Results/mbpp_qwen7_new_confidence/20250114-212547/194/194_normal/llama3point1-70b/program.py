import re

def find_adverb_position(sentence):
    adverbs = ['clearly', 'seriously', 'unfortunately']
    words = sentence.split()
    for i, word in enumerate(words):
        if word.strip('!!') in adverbs:
            return (i, len(sentence[:sentence.find(word)]), word.strip('!!'))
    return None
