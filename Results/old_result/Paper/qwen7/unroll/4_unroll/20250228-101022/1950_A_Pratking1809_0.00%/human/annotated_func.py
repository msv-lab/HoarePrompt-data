#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output state will consist of 'STAIR', 'PEAK', or 'NONE' printed for each iteration of the loop based on the input values. The specific sequence of these outputs depends on the input provided during each iteration. Since the exact inputs are not specified, the output will be a series of 'STAIR', 'PEAK', or 'NONE' lines corresponding to the conditions met in each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \(a\), \(b\), and \(c\). For each test case, it checks if \(a < b < c\) and prints 'STAIR' if true; if \(a < b > c\), it prints 'PEAK'; otherwise, it prints 'NONE'. The function reads the number of test cases from the first input, followed by the values for each test case. After processing all test cases, it outputs a series of 'STAIR', 'PEAK', or 'NONE' lines corresponding to the conditions met in each test case.

