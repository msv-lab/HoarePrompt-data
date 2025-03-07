#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 2:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: The value of `t` remains unchanged, and `n` remains unchanged. The final values of `s`, `a`, `b`, and `c` are based on the last iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of lowercase English letters and prints 'NO' if the string contains exactly two distinct characters, otherwise it prints 'YES'. If the string is not already sorted in ascending order, it prints the string sorted in ascending order; otherwise, it prints the string sorted in descending order.

