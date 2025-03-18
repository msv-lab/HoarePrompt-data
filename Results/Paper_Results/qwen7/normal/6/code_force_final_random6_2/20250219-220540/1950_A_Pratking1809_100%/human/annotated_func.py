#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `q` is a positive integer, `i` is 3, `a`, `b`, and `c` are integers entered by the user, and they are assigned to the variables `a`, `b`, and `c` respectively. Regardless of the condition `a < b < c` or `a < b > c`, the values of `a`, `b`, and `c` remain unchanged.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(a\), \(b\), and \(c\). For each test case, it prints 'STAIR' if \(a < b < c\), 'PEAK' if \(a < b > c\), and 'NONE' otherwise. The function reads the number of test cases from the user and then iterates through each case, performing the necessary comparisons and printing the result. After processing all test cases, the function concludes without returning any value.

