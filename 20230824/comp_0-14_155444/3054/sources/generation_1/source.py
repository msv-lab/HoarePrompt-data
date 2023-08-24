
def count_syllables(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    word = word.lower()
    count = 0

    if word[-1] == 'e' and (len(word) == 1 or (len(word) == 2 and word[0] == 'l')):
        # Exception: silent 'e' at the end of the word
        return count

    i = 0
    while i < len(word):
        if word[i] in vowels:
            count += 1

            if i+1 < len(word) and word[i] == 'y' and word[i+1] in vowels:
                # Exception: 'y' followed by another vowel
                count -= 1

            i += 1
        elif i+1 < len(word) and word[i:i+2] == 'qu':
            # Exception: 'qu' counted as a single consonant
            i += 2
        elif i+2 < len(word) and word[i:i+3] == 'end' and word[i+1:i+3] == 'es':
            # Exception: 'end' followed by 'es' at the end of the word
            break
        else:
            # Count the consecutive consonants as separate syllables
            while i < len(word) and word[i] not in vowels:
                i += 1

    return count


def haiku_check(line):
    words = line.split()
    syllables = []

    for word in words:
        syllables.append(count_syllables(word))

    haiku = []
    line_syllables = 0
    line_words = []
    
    for word, syllable_count in zip(words, syllables):
        if line_syllables + syllable_count <= 5:
            line_syllables += syllable_count
            line_words.append(word)
        elif len(haiku) < 2:
            haiku.append(' '.join(line_words))
            line_syllables = syllable_count
            line_words = [word]
        else:
            # Haiku cannot have more than 3 lines
            return line
    
    if len(haiku) < 2:
        # Haiku must have at least 3 lines
        return line
    
    haiku.append(' '.join(line_words))
    
    return '\n'.join(haiku)


line = input()
haiku = haiku_check(line)
print(haiku)
