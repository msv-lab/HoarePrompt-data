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
        
    #State: The output state will consist of 'YES', 'NO', 'Yes', or 'No' printed based on the conditions inside the loop for each iteration from 0 to a-1. The specific sequence of these outputs depends on the input values provided for 'b' and 'c' in each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers `b` and `c`. It prints one of four possible responses ('YES', 'NO', 'Yes', or 'No') for each test case based on the relationship between `b` and `c`. If `b` equals `c`, it prints 'YES'. If `b` is less than `c`, it prints 'NO'. If `b` and `c` have the same parity (both even or both odd), it prints 'Yes'. Otherwise, it prints 'No'. The function does not return any value but modifies the console output by printing the results of each test case.

