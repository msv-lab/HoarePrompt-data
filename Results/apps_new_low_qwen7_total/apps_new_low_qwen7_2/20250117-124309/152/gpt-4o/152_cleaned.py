def func_1(c):
    return c in 'aeiou'

def func_2(block):
    if len(block) < 3:
        return False
    first_consonant = block[0]
    for c in block:
        if c != first_consonant:
            return True
    return False

def func_3(word):
    n = len(word)
    result = []
    i = 0
    while i < n:
        start = i
        while i < n and (not func_1(word[i])):
            i += 1
        if i - start >= 3 and func_2(word[start:i]):
            result.append(word[start:start + 2])
            start += 2
            while start < i:
                result.append(word[start:start + 1])
                start += 1
        else:
            result.append(word[start:i])
        while i < n and func_1(word[i]):
            i += 1
        result.append(word[start:i])
    return ' '.join(result)
if __name__ == '__main__':
    word = input().strip()
    print(func_3(word))