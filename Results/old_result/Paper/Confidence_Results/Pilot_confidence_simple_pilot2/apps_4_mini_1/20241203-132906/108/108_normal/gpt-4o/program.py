s = input()

# We need to find a subsequence that represents a number divisible by 64.
# In binary, 64 is represented as 1000000. Thus, we need to find at least one '1'
# followed by six '0's in the string.

# Check if there is at least one '1' in the string
if '1' not in s:
    print("no")
else:
    # Find the first '1' and check if there are at least six '0's after it
    index_of_first_one = s.find('1')
    remaining_string = s[index_of_first_one+1:]
    count_of_zeros = remaining_string.count('0')
    
    if count_of_zeros >= 6:
        print("yes")
    else:
        print("no")
