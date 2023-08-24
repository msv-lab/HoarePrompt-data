n = int(input())
s = input()

# initialize variables
substrings = [] # to store the valid substrings
current_substring = "" # to store the current substring being formed
count_0 = 0 # to count the number of zeroes
count_1 = 0 # to count the number of ones

# iterate through each character in s
for char in s:
    # if character is '0', increment count_0
    if char == '0':
        count_0 += 1
    # if character is '1', increment count_1
    if char == '1':
        count_1 += 1
    
    # if count of zeroes and ones are equal, we have formed a valid substring
    if count_0 == count_1:
        substrings.append(current_substring + char) # add the current substring to the list
        current_substring = "" # reset current_substring
        count_0 = 0 # reset count_0
        count_1 = 0 # reset count_1
    else:
        current_substring += char # append the current character to the current_substring

# print the minimal number of strings and the substrings
print(len(substrings))
print(" ".join(substrings))