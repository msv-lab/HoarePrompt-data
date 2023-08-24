n = int(input())
s = input()

substrings = []
current_substring = ""
count_0 = 0
count_1 = 0

for char in s:
    if char == '0':
        count_0 += 1
    else:
        count_1 += 1
    
    if count_0 == count_1:
        substrings.append(current_substring + char)
        current_substring = ""
        count_0 = 0
        count_1 = 0
    elif count_0 > 0 and count_1 > 0:
        substrings.append(current_substring)
        current_substring = char
        if char == '0':
            count_0 = 1
            count_1 = 0
        else:
            count_0 = 0
            count_1 = 1
    else:
        current_substring += char

if current_substring != "":
    substrings.append(current_substring)

print(len(substrings))
print(" ".join(substrings))