#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: Output State: The output consists of multiple lines where each line contains two integers. For each test case, the output starts with two lines `1 1` and `1 2`. Then, for each integer `n` in the range from 3 to `n`, there is a line containing `i i`. The total number of lines depends on the value of `t` (the number of test cases) and `n` (the value of `n` for each test case).
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it outputs a series of lines. Each line contains two identical integers starting from 1 up to `n`. Specifically, it first prints `1 1` and then `1 2`, followed by lines of the form `i i` for each integer `i` from 3 to `n`. The function reads the number of test cases `t` and the value of `n` for each test case from standard input.

