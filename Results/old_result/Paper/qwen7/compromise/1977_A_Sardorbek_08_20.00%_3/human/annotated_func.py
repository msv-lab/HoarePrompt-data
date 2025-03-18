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
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: The output state will consist of 'YES', 'NO', 'Yes', or 'No' printed based on the conditions inside the loop for each iteration from 0 to a-1. The specific sequence of outputs depends on the values of b and c entered during each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( b \) and \( c \) (where \( 1 \leq b, c \leq 100 \)). For each test case, it prints 'YES' if \( b \) equals \( c \), 'NO' if \( b \) is less than \( c \), 'Yes' if both \( a \) and \( b \) have the same parity (both even or both odd), and 'No' otherwise. The function does not return any value but prints the results for each test case.

