#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: The output state will consist of pairs of integers printed based on the comparison of the integers provided in each input line for `x` iterations. For each iteration, if the first integer is less than the second integer, the first integer is printed followed by the second integer; otherwise, the second integer is printed followed by the first integer. The total number of printed pairs will be equal to `x`. The specific values printed will depend on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each involving two integers \(x\) and \(y\). For each test case, it compares \(x\) and \(y\), and prints them in ascending order. If \(x\) is less than \(y\), it prints \(x\) followed by \(y\); otherwise, it prints \(y\) followed by \(x\). The function does not return any value but outputs the sorted pairs of integers for each test case.

