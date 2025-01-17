def find_adverb_position(sentence):
    words = sentence.split()
    for word in words:
        if word.endswith("ly"):
            start = sentence.find(word)
            end = start + len(word) - 1
            return (start, end, word)
    return None  # If no adverb is found, return None

# Test cases
assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly!!')
assert find_adverb_position("seriously!! there are many roses") == (0, 9, 'seriously!!')
assert find_adverb_position("unfortunately!! sita is going to home") == (0, 13, 'unfortunately!!')
