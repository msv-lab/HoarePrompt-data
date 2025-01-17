def xor_sequences(x, y):
    result = []
    for i in range(max(x, y) + 1):
        result.append(i ^ x)
    return result

def longest_common_subsegment(x, y):
    a = xor_sequences(x, y)
    b = xor_sequences(y, x)
    longest = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                current = 1
                while i + current < len(a) and j + current < len(b) and a[i + current] == b[j + current]:
                    current += 1
                longest = max(longest, current)

    return longest