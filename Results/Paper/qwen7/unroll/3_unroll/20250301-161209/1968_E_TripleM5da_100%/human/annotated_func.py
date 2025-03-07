#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: The output will consist of a series of lines where each line contains two integers. For each test case, there will be exactly `n-2` lines starting from "1 1" and "1 2", followed by lines ranging from "3 3" to "n n". The total number of lines for each test case will be `n`. The value of `t` does not affect the output format or content since it only determines how many test cases are processed.
#Overall this is what the function does:The function processes multiple test cases defined by the integer `t`. For each test case, it outputs a sequence of lines containing pairs of integers. Specifically, it starts with the pair "1 1", followed by "1 2", and then continues with pairs ranging from "3 3" to "n n" (inclusive), where `n` is the second parameter for each test case. The total number of lines output for each test case is `n`, regardless of the value of `t`.

