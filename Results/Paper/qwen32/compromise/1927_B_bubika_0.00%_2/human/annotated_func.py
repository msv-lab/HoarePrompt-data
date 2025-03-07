#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; n is the input integer; s is the list of integers provided as input; r is a string formed by concatenating characters from a based on the indices of elements in s and their occurrences; b is a list where each element reflects the total count of occurrences of its corresponding element in s from all iterations.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `s` of `n` integers. For each test case, it constructs and prints a string `r` of lowercase Latin letters based on the indices in `s` and their occurrences.

