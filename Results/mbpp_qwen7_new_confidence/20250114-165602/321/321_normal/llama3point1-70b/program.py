def count_reverse_pairs(strings):
    count = 0
    for s in strings:
        reverse_s = s[::-1]
        if reverse_s in strings and reverse_s != s:
            count += 1
            strings.remove(reverse_s)
    return count
