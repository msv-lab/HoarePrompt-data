#State of the program right berfore the function call: n is an integer such that 1 <= n <= 500, and s is a string of length n consisting of lowercase Latin letters.
def func():
    n = int(input())
    s = input()
    operations = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            operations += 1
        
    #State of the program after the  for loop has been executed: `operations` is equal to the number of distinct character transitions in `s` plus one, `s` is a string of length `n`, and `n` is an integer (1 <= n <= 500).
    print(operations)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 500) and a string `s` of length `n` consisting of lowercase Latin letters. It calculates the number of distinct character transitions in the string `s` and adds one to the count to account for the initial character. The final count is printed as the output.

