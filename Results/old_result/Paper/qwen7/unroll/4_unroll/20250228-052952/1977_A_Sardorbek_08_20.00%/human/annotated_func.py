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
        
    #State: The output state will consist of 'YES', 'NO', 'Yes', or 'No' printed based on the conditions inside the loop for each iteration from 0 to a-1. The specific sequence of these outputs depends on the values of b and c entered during each iteration.
#Overall this is what the function does:The function processes multiple pairs of positive integers (b, c) within the range of 1 to 100. For each pair, it checks the relationship between b and c and prints one of four possible responses: 'YES', 'NO', 'Yes', or 'No'. The final state of the program consists of a series of these printed responses, one for each input pair.

