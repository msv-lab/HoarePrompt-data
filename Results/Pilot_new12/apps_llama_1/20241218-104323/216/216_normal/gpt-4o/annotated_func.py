#State of the program right berfore the function call: The input consists of an integer n representing the length of the string s, and a string s consisting of lowercase and uppercase Latin letters, where 1 <= n <= 200 and the length of s is equal to n.
def func():
    n = int(input())
    s = input()
    max_count = 0
    current_set = set()
    current_count = 0
    for char in s:
        if char.islower():
            if char not in current_set:
                current_set.add(char)
                current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_set.clear()
            current_count = 0
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `s` is the input string, `max_count` is the maximum count of consecutive unique lowercase letters separated by non-lowercase characters, `current_set` is either an empty set (if `s` ends with a non-lowercase character) or contains the unique lowercase letters after the last non-lowercase character, and `current_count` is either 0 (if `s` ends with a non-lowercase character) or the count of unique lowercase letters after the last non-lowercase character.
    max_count = max(max_count, current_count)
    print(max_count)
#Overall this is what the function does:The function accepts an integer `n` representing the length of a string `s`, and a string `s` consisting of lowercase and uppercase Latin letters. It then calculates and prints the maximum count of consecutive unique lowercase letters separated by non-lowercase characters in the string `s`. The function considers all substrings of `s` separated by non-lowercase characters and keeps track of the maximum count of unique lowercase letters in these substrings. The final state of the program includes the printed maximum count of unique lowercase letters, and the input variables `n` and `s` remain unchanged. The function handles edge cases where the string `s` starts or ends with a non-lowercase character, or contains consecutive non-lowercase characters, and correctly updates the maximum count accordingly. The function does not return any value, but instead prints the result to the console.

