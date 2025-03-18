#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that for each test case, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: t is 0, n, s, b, and r reflect the state after the last test case was processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `s` of `n` integers. It then constructs and prints a string of length `n` consisting of lowercase Latin letters, where each letter's occurrence in the string matches the counts specified in the list `s`.

