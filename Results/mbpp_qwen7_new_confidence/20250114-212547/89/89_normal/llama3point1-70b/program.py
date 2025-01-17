def count_char_position(s):
    s = s.lower()
    count = 0
    for i, char in enumerate(s):
        if ord(char) - 96 == i + 1:
            count += 1
    return count
