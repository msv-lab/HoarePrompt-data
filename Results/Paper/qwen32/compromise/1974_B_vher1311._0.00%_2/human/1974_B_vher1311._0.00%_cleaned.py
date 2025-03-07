def func_1(s):
    unique_chars = sorted(list({char for char in s}))
    (i, j) = (0, len(unique_chars) - 1)
    for char in s:
        if char in unique_chars:
            s = s.replace(char, unique_chars[j])
            j -= 1
        else:
            unique_chars.insert(i, char)
            i += 1
            j += 1
    return ''.join(unique_chars)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = input()
        encoded_str = func_1(b)
        print(encoded_str)