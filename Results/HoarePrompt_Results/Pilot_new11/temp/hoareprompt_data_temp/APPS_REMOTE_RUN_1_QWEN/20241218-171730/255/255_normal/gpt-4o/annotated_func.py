#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `s` is a string entered by the user, `n` is the original input integer, `operations` is the count of character transitions in `s` where each character at index `i` (for `i` in range 1 to `n-1`) is different from the previous character `s[i-1]`.
    print(operations)
#Overall this is what the function does:The function `func` accepts an integer `n` (where 1 ≤ n ≤ 500) and a string `s` of length `n` consisting of lowercase Latin letters. It calculates and prints the number of transitions in the string `s`, where a transition is defined as a character at index `i` (for `i` in range 1 to `n-1`) being different from the previous character `s[i-1]`. The function does not return any value; instead, it prints the total number of transitions found in the string `s`.

