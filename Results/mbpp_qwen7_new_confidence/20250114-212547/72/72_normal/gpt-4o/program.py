def long_words(n, sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words that are longer than n characters
    result = [word for word in words if len(word) > n]
    
    return result

# Test cases
assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
assert long_words(2, "writing a program") == ['writing', 'program']
assert long_words(5, "sorting list") == ['sorting']
