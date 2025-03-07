#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, a, b, and c are digits (integers) such that 0 <= a, b, c <= 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The values of `t`, `a`, `b`, and `c` remain unchanged, but the loop will have printed 'STAIRS', 'PEAK', or 'NONE' for each of the `t` test cases based on the conditions provided.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 1000`. For each of the `t` test cases, it reads three digits `a`, `b`, and `c` (integers where `0 <= a, b, c <= 9`). Based on the values of `a`, `b`, and `c`, the function prints 'STAIRS' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only prints the results for each test case. After the function concludes, the values of `t`, `a`, `b`, and `c` are not retained, and the program state is unchanged except for the output printed to the console.

