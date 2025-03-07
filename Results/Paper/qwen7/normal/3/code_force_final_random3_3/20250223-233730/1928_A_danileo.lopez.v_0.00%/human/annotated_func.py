#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: After all iterations of the loop have finished, `t` will be 0, and the values of `a` and `b` will be the last integers entered by the user during the final iteration of the loop. No changes are made to `a` and `b` inside the loop based on the conditions given.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, a, and b. It checks if t is within the range 1 to 10^4 and both a and b are within the range 1 to 10^9. If a or b is even, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, t will be 0, and the final values of a and b will be the last integers entered during the final iteration of the loop.

