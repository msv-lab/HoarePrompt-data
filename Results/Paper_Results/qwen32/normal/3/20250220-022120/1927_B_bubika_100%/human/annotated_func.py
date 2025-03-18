#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that for each test case, a valid string s exists.
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
        
    #State: The final output state after all iterations is the concatenation of the strings `r` for each of the `t` test cases. Each `r` is formed by appending characters from `a` based on the values in the corresponding `s`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `s` of `n` integers. For each test case, it constructs and prints a string `r` where each character in `r` is determined by the corresponding integer in `s`, mapping to characters in the alphabet based on a frequency count mechanism.

