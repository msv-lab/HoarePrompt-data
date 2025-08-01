#State of the program right berfore the function call: The function is expected to handle multiple test cases, where each test case consists of three digits a, b, and c such that 0 <= a, b, c <= 9. The number of test cases, t, is a positive integer where 1 <= t <= 1000.
def func():
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The values of `a`, `b`, and `c` are not retained after each iteration of the loop, and the loop runs `q` times. For each test case, the loop prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The variables `t` and `mn` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `q` from the user input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` (where 0 <= a, b, c <= 9) from the user input. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value. After the function concludes, the variables `q`, `a`, `b`, and `c` are not retained, and any other variables outside the function remain unchanged.

