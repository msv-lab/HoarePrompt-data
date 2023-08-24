def longest_duplicate_string(length, string):
    max_length = 0
    duplicates = set()
    
    for i in range(length - 1):
        for j in range(i + 1, length):
            if string[i:j+1] in duplicates:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
            else:
                duplicates.add(string[i:j+1])
    
    return max_length

L = int(input())
s = input()

result = longest_duplicate_string(L, s)
print(result)