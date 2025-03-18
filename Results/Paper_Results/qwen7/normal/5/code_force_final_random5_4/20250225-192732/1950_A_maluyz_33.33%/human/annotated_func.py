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
        
    #State: t is an integer between 1 and 1000 inclusive, i equals t-1, a, b, and c are integers where their values are input from the user during each iteration of the loop. The final output will consist of 'STAIR', 'PEAK', or 'NONE' printed for each set of inputs (a, b, c) based on the conditions provided in the loop body.
#Overall this is what the function does:The function reads a series of test cases, each containing three integers \(a\), \(b\), and \(c\). For each set of integers, it determines whether the sequence forms a 'STAIR' (if \(a < b < c\)), a 'PEAK' (if the maximum value among \(a\), \(b\), and \(c\) is \(b\)), or 'NONE' otherwise. It prints the result for each test case.

