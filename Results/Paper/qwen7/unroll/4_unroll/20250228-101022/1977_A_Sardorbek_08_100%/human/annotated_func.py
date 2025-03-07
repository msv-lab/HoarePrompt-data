#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: The output state will consist of 'YES', 'NO', 'Yes', or 'No' printed for each iteration of the loop based on the conditions provided. The specific sequence of these outputs depends on the values of `b` and `c` entered during each iteration. Since the initial value of `t` does not affect the loop itself, the output state will be determined solely by the loop's execution.
#Overall this is what the function does:The function processes a series of pairs of positive integers \(b\) and \(c\) (where \(1 \leq b, c \leq 100\)) based on a given count \(t\) (where \(1 \leq t \leq 100\)). For each pair, it prints 'YES' if \(b\) equals \(c\), 'NO' if \(b\) is less than \(c\), 'Yes' if both \(b\) and \(c\) have the same parity (both even or both odd), and 'No' otherwise. The function does not return any value.

