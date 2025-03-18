#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The output state will consist of a series of lines, each containing either 'STAIR', 'PEAK', or 'NONE', depending on the input values for each iteration of the loop. Specifically, for each line of input (a, b, c) within the range of n, the output will be 'STAIR' if a < b < c, 'PEAK' if a < b and b > c, and 'NONE' otherwise. The number of lines in the output will be equal to n, and the exact content of each line will depend on the input provided during each iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers \(a\), \(b\), and \(c\). For each test case, it determines whether the sequence \(a, b, c\) forms a 'STAIR' (if \(a < b < c\)), a 'PEAK' (if \(a < b\) and \(b > c\)), or neither ('NONE'). It then prints the corresponding label for each test case. The function does not return any value; instead, it outputs the results directly.

