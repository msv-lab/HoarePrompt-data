#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer between 1 and 1000 inclusive, `i` is 999 (since the loop runs from `i=0` to `i=t-1`), and `a`, `b`, and `c` are the integers entered by the user for the last iteration of the loop.
#Overall this is what the function does:The function processes up to 1000 sets of three integers (a, b, and c) where each integer is between 0 and 9. For each set, it prints 'STAIR' if a < b < c, 'PEAK' if a < b > c, and 'NONE' otherwise. After processing all sets, it does not return any value.

