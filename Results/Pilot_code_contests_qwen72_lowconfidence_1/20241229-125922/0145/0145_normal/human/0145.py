prime = 2**32 -1
english_base = 30;


class Hasher(object):
    def __init__(self, word, modulo = prime):
        self.word = word
        self.modulo = modulo
        self.h = self.compute_hashes(self.word)
        self.powers = self.compute_power(len(self.word))

    def substring_hash(self, i, j):
        result = self.h[j] - self.h[i] * self.powers[j-i]
        return result % self.modulo

    
    def compute_hashes(self, word, base=english_base, modulo=prime):
        h = [None for _ in range(len(word) + 1)]
        h[0] = 0
        for i in range(len(word)):
            letter_as_number = (ord(word[i]) - ord('a') + 1)
            h[i + 1] = h[i] * base + letter_as_number
            h[i + 1] %= modulo
        return h


    def compute_power(self, n, base=english_base, modulo=prime):
        powers = [None for _ in range(n+1)]
        powers[0] = 1
        for i in range(n):
            powers[i+1] = (powers[i] * base) % modulo
        return powers
    

def splitter(text1, text2, i1, j1, i2, j2, hash1, hash2):
    mid1 = int((j1+i1)/2)
    mid2 = int((j2+i2)/2)
    if (j1-i1)%4 != 0 or (j1-i1)==2:
        a1 = hash1.substring_hash(i1,mid1)
        a2 = hash1.substring_hash(mid1,j1)
        b1 = hash2.substring_hash(i2,mid2)
        b2 = hash2.substring_hash(mid2,j2)
        if a1 == b1:
            return a2 == b2
        elif a2 == b1:
            return a1 == b2
        return False
    return (splitter(text1, text2, i1, mid1, i2, mid2, hash1, hash2) and splitter(text1, text2, mid1, j1, mid2, j2, hash1, hash2)) or (splitter(text1, text2, i1, mid1, mid2, j2, hash1, hash2) and splitter(text1, text2, mid1, j1, i2, mid2, hash1, hash2))

def equivalent_substrings(text1, text2):
    hash1 = Hasher(text1)
    hash2 = Hasher(text2)

    return splitter(text1, text2, 0, len(text1), 0, len(text2), hash1, hash2)


def main():
    s1 = raw_input();
    s2 = raw_input();
    print(equivalent_substrings(s1,s2))


if __name__=='__main__':
    main()
