def long_words(n, sentence):
    return [word for word in sentence.split() if len(word) > n]
