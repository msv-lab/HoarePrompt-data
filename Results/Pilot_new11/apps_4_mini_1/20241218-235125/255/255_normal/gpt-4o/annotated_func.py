#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `s` is a string of length `n`, `operations` is equal to the number of character transitions in `s` plus one (the initial operations count), and `n` is an integer between 1 and 500.
    print(operations)
#Overall this is what the function does:The function accepts an integer `n` (where 1 <= n <= 500) and a string `s` of length `n` consisting of lowercase Latin letters. It counts the number of transitions between different characters in the string (i.e., when two consecutive characters are different) and adds one to this count (to account for the initial state). The final output is the total count of character transitions plus one, which is printed to the console. The function does not handle cases where the inputs are not within the specified bounds, nor does it validate that the string `s` is exactly of length `n`. The output is a single integer representing the computed number of operations.

