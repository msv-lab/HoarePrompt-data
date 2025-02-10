#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
def func():
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = ''
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        
        print(t)
        
        print(*ans)
        
    #State: `t` is 1000, `i` is 1000, `x` is 1, `max` is -100000000, `min` is 100000000, `ans` is a string containing the sequence of alternating `max` and `min` values from 100000000 down to -100000000 and back up to 100000000 in reverse order.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads an integer `X` (2 ≤ X ≤ 10^18) and an implied integer `t` (1 ≤ t ≤ 1000). It then performs a series of operations on `X`, tracking the number of steps (`t`) taken until `X` becomes 1. During these operations, it alternates between decrementing `X` by 1 when `X` is odd and halving `X` when `X` is even, recording a sequence of maximum and minimum values (`max` and `min`) in reverse order. Finally, it prints the count of steps (`t`) and the recorded sequence of values.

