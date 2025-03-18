#State of the program right berfore the function call: For each test case, n is an integer such that 1 <= n <= 26, and k is an integer such that 1 <= k <= 26. The number of test cases t is an integer such that 1 <= t <= 676.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: The output state is a concatenation of the printed strings for each iteration. Specifically, for each iteration, if `k` is 1, `n` repetitions of the character 'a' are printed. Otherwise, `(2 - (n == 1))` repetitions of the string `s` (which consists of the first `k` letters of the English alphabet) are printed.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`. For each test case, it prints a string consisting of the first `k` letters of the English alphabet, repeated a number of times based on the value of `n`. Specifically, if `k` is 1, it prints `n` repetitions of the character 'a'. Otherwise, it prints the string of the first `k` letters, repeated either once or twice depending on whether `n` is 1 or greater than 1.

