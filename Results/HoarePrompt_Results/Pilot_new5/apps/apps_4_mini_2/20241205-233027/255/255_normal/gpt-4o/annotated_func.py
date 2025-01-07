#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting only of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 500, `s` is a string of length `n`, `operations` is the count of transitions between different characters in the string `s` (where a transition is defined as `s[i]` being different from `s[i - 1]`), and `i` is equal to `n - 1`. If `n` is 1, the loop does not execute, and `operations` remains 1.
    print(operations)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 500) and a string `s` of length `n` consisting of lowercase Latin letters. It counts the number of transitions between different characters in the string (where a transition is defined as a change from one character to a different one) and prints this count. If the string consists of only one unique character, it will print 1, as there are no transitions. The function does not return any value; it only outputs the count of transitions.

