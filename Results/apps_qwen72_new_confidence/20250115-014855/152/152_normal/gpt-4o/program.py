def is_vowel(c):
    return c in 'aeiou'

def has_typo(block):
    if len(block) < 3:
        return False
    first_consonant = block[0]
    for c in block:
        if c != first_consonant:
            return True
    return False

def correct_typo(word):
    n = len(word)
    result = []
    i = 0

    while i < n:
        start = i
        while i < n and not is_vowel(word[i]):
            i += 1
        if i - start >= 3 and has_typo(word[start:i]):
            result.append(word[start:start+2])
            start += 2
            while start < i:
                result.append(word[start:start+1])
                start += 1
        else:
            result.append(word[start:i])
        while i < n and is_vowel(word[i]):
            i += 1
        result.append(word[start:i])
        
    return ' '.join(result)

if __name__ == "__main__":
    word = input().strip()
    print(correct_typo(word))
