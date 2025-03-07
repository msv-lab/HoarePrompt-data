#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: `t` is 0, `b` is a list of 26 zeros with the elements at the indices corresponding to the integers in `s` incremented by the number of times those values appear in `s` across all iterations, `n` is an input integer greater than 0, `s` is a list of integers provided by the user, `r` is a string containing the characters from the string `a` at the indices corresponding to the integers in `s`, concatenated in the order they appear in `s` for each iteration.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `s` of `n` integers. It then maps each integer in `s` to a character in the string 'abcdefghijklmnopqrstuvwxyz' based on the integer's value, and constructs a string `r` by concatenating these characters in the order they appear in `s`. The function prints the string `r` for each test case. After processing all test cases, the function does not return any value. The final state of the program is that `t` is 0, `b` is a list of 26 zeros (with the elements at the indices corresponding to the integers in `s` incremented by the number of times those values appear in `s` across all iterations), `n` is the last input integer greater than 0, `s` is the last list of integers provided by the user, and `r` is the last constructed string.

