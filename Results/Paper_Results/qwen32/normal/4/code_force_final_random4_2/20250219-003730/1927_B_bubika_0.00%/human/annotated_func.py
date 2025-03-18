#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: `t` is an integer such that `t` <= 10^4, `n` is the input integer for the last test case, `s` is a list of integers obtained from the last input, `b` is a list of integers where each element represents the total count of the corresponding element in `s` across all test cases, and `r` is a string formed by concatenating characters from `a` corresponding to each element in `s` for the last test case.
#Overall this is what the function does:The function reads multiple test cases. For each test case, it reads an integer `n` and a list `s` of `n` integers. It then constructs and prints a string `r` by mapping each integer in `s` to a corresponding character in the alphabet, where each integer `i` in `s` maps to the character at index `i` in the list `b`, and `b` keeps track of the count of each integer encountered across all test cases. The final output for each test case is the constructed string `r`.

