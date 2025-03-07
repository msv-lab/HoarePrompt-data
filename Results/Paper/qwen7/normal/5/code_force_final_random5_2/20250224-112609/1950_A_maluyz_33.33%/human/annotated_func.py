#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: `t` is an integer between 1 and 1000, `i` is 999 (since the loop runs `t` times), `a`, `b`, and `c` are assigned the values of three integers entered by the user during the last iteration of the loop. If `a < b < c` is true during the last iteration, the values of `a`, `b`, and `c` remain unchanged. Otherwise, the values of `a`, `b`, and `c` remain unchanged.
    #
    #This means that after the loop completes all its iterations, the variable `t` will be equal to the initial input integer, `i` will be `t-1`, and `a`, `b`, and `c` will hold the values from the last set of inputs provided by the user.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of three integers \(a\), \(b\), and \(c\) within the range [0, 9]. For each test case, it prints one of three strings: "STAIR" if \(a < b < c\), "PEAK" if \(b\) is the maximum value among \(a\), \(b\), and \(c\), and "NONE" otherwise. After processing all test cases, it outputs nothing and ends.

