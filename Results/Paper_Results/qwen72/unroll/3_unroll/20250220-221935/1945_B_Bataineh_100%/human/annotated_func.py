#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has completed all iterations, and the values of t, a, b, and m remain unchanged as they were input for each test case. The loop has printed a result for each test case based on the conditions provided in the loop body.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads three integers `a`, `b`, and `m` from the input. Based on the values of `a`, `b`, and `m`, the function prints a specific integer result for each test case. The final state of the program after the function concludes is that `t` test cases have been processed, and the corresponding results have been printed to the console. The input variables `t`, `a`, `b`, and `m` are not modified and retain their initial values as provided in each test case.

