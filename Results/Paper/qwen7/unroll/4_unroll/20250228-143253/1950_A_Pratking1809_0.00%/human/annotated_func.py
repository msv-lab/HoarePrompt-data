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
        
    #State: The output state will consist of q lines, each containing either 'STAIR', 'PEAK', or 'NONE' based on the conditions evaluated for each set of inputs (a, b, c) provided by the user during the loop iterations. The initial values of `t`, `q`, and `mn` remain unchanged.
#Overall this is what the function does:The function reads a series of test cases from the user, where each test case consists of three integers \(a\), \(b\), and \(c\). For each test case, it checks the relationship between these integers and prints one of three possible outputs: 'STAIR', 'PEAK', or 'NONE'. After processing all test cases, it does not return any value but prints the results directly. The initial values of \(t\) and \(q\) remain unchanged throughout the function's execution.

