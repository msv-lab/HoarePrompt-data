#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of three integers a, b, m where 1 ≤ a, b, m ≤ 10^18, representing the frequency of launching for the first installation, the second installation, and the visibility duration of a firework, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: `t` is an integer input by the user within the range 1 ≤ t ≤ 10^4, `i` is `t`, `a` is the last integer input by the user, `b` is the second last integer input by the user, `m` is the third last integer input by the user, and `mn` is the value of `min(a, b) + m`. If `m` is divisible by both `a` and `b`, and neither `a` nor `b` is 1, the program maintains these values. Otherwise, the program also maintains these values.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`, representing the frequency of launching for two installations and the visibility duration of a firework, respectively. It calculates the minimum of `a` and `b`, adds `m` to it, and then prints a result based on whether `m` is divisible by both `a` and `b` (and neither `a` nor `b` is 1). The function outputs a series of results, one for each test case, and the final state of the program includes the processed values of `t`, `a`, `b`, and `m` for the last test case.

