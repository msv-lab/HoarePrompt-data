#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: Output State: The output state consists of `t` lines, where each line contains the value of `x` divided by 2 (integer division), for each test case provided.
#Overall this is what the function does:The function reads an integer `t` and then processes `t` test cases. For each test case, it reads an integer `x` and prints the result of integer division of `x` by 2. After processing all test cases, the function does not return any value.

