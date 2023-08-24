s = input()
good_letters = input()
k = int(input())

# Create a set to store the distinct good substrings
good_substrings = set()

# Iterate through each possible starting position of the substring
for i in range(len(s)):
    bad_count = 0 # Counter for the number of bad letters in the current substring
    
    # Iterate through each letter in the substring starting from position i
    for j in range(i, len(s)):
        letter = s[j]
        
        # If the letter is bad, increment the bad count
        if good_letters[ord(letter) - ord('a')] == '0':
            bad_count += 1
        
        # If the bad count is within the acceptable limit (k), add the current substring to the set
        if bad_count <= k:
            good_substrings.add(s[i:j+1])
        
        # If the bad count exceeds the acceptable limit, break the loop as further extensions of the substring will also exceed the limit
        else:
            break

# Output the number of distinct good substrings
print(len(good_substrings))