#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: a series of strings `r` for each test case, where each string `r` is constructed by the described process.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it constructs and prints a string of lowercase Latin letters based on the input list.

