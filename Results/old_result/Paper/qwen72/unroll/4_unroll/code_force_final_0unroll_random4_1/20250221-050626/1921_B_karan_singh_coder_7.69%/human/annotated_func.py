#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 10^5, s and f are strings of length n consisting of characters '0' and '1', and the sum of n over all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        s = input()
        
        t = input()
        
        s1 = s.count('1')
        
        t1 = t.count('1')
        
        cnt = 0
        
        for i in range(n):
            cnt += s[i] != t[i]
        
        if s1 == t1:
            print(s1 if cnt else 0)
        else:
            d = abs(s1 - t1)
            print((cnt - d) // 2 + d)
        
    #State: The loop has finished executing for all test cases. The values of `t`, `n`, `s`, and `f` are unchanged from the initial state, as they are re-assigned within each iteration of the loop. The variables `s1`, `t1`, `cnt`, and `d` are local to each iteration and do not persist outside the loop.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of an integer `n` and two strings `s` and `t` of length `n` containing only '0' and '1'. For each test case, it calculates the number of positions where `s` and `t` differ and the number of '1's in each string. If the number of '1's in `s` and `t` is the same, it prints the number of '1's if there are any differences, otherwise it prints 0. If the number of '1's in `s` and `t` is different, it calculates and prints a value based on the differences and the absolute difference in the number of '1's. After processing all test cases, the function concludes. The function does not return any value.

