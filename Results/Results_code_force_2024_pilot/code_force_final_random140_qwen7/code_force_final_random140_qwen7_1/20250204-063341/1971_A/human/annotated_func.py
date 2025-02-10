#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: Output State: `t` is 1, `a` is an integer from the input, `b` is an integer from the input.
    #
    #After the loop executes all its iterations, `t` will be reduced to 1 and will continue to decrease until it reaches 0, at which point the loop will terminate. At each iteration, the values of `a` and `b` are updated based on the input provided by the user. Therefore, after all iterations, `t` will be 1, and `a` and `b` will hold the values of the last pair of integers entered by the user.
#Overall this is what the function does:The function processes up to 100 test cases, each consisting of two integers `a` and `b`. For each test case, it prints the larger of the two integers followed by the smaller one. After processing all test cases, the function ends with `t` set to 1, reflecting the number of remaining test cases (which would be 0 if all cases were processed).

