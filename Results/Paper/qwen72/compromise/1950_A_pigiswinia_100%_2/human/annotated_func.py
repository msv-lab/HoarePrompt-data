#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a list or tuple of three digits a, b, and c such that 0 <= a, b, c <= 9. The number of test cases t should be a non-negative integer where 1 <= t <= 1000.
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
        
    #State: The loop will execute `t` times, and for each iteration, it will read three digits `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it will print 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The values of `a`, `b`, and `c` will be overwritten in each iteration, and the loop variable `i` will increment from 0 to `t-1`. After the loop finishes, the values of `a`, `b`, and `c` will be the values read in the last iteration, and `i` will be equal to `t`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where `1 <= t <= 1000`. For each test case, it reads three integers `a`, `b`, and `c` (where `0 <= a, b, c <= 9`) from the input. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. After processing all test cases, the function does not return any value, but the final state of the program includes the values of `a`, `b`, and `c` from the last test case, and the loop variable `i` will be equal to `t-1`.

