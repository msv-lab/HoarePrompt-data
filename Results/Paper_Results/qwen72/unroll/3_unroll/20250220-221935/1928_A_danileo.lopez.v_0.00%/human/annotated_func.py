#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a and b are integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            print('Yes')
        else:
            print('No')
        
    #State: The loop has executed t times, and for each iteration, if either a or b is even, 'Yes' is printed; otherwise, 'No' is printed. The values of t, a, and b remain unchanged as they are input values and are not modified within the loop.
#Overall this is what the function does:The function `func` processes `t` test cases, where `t` is an integer such that 1 <= t <= 10^4. For each test case, it reads two integers `a` and `b` such that 1 <= a, b <= 10^9. The function prints 'Yes' if either `a` or `b` is even, and 'No' if both `a` and `b` are odd. The function does not return any value. After the function concludes, the values of `t`, `a`, and `b` are not modified and remain as they were read from input.

