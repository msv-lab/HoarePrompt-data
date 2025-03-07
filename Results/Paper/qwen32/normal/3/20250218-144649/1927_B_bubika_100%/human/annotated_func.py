#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: `t` is 0, `n` is the number of elements in the last `s`, `s` is the list of integers from the last test case, `a` is 'abcdefghijklmnopqrstuvwxyz', `b` is the cumulative counts of each index across all test cases, and `r` is the string constructed for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `s` of `n` integers. For each test case, it constructs and prints a string `r` of length `n` where each character is a lowercase Latin letter determined by the corresponding integer in the list `s`.

