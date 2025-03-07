#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: Output State: `t` is an integer between 1 and 1000, `i` is 999 (since the loop runs from `i` in `range(t)`), `a`, `b`, and `c` are integers assigned from the input split for the last iteration of the loop. The values of `t`, `i`, `a`, `b`, and `c` remain unchanged regardless of whether the conditions `a < b < c` or `a < b > c` are met during any iteration of the loop.
#Overall this is what the function does:The function processes up to 1000 test cases, where for each test case, it reads three integers \(a\), \(b\), and \(c\) within the range 0 to 9. Based on the values of these integers, it prints either "STAIRS" if \(a < b < c\), "PEAK" if \(a < b > c\), or "NONE" otherwise. After processing all test cases, the function does not return anything but prints the results for each test case.

