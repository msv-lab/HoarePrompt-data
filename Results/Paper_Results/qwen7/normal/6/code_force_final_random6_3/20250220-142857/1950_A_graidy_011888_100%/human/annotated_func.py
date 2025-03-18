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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, i is equal to n-1, a, b, and c are integers entered by the user during the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each containing three integers \(a\), \(b\), and \(c\) (where \(0 \leq a, b, c \leq 9\)). For each test case, if the integer \(t\) (which is read at the beginning and is the number of test cases) is within the range 1 to 1000, the function checks the relationship between \(a\), \(b\), and \(c\). It then prints 'STAIR' if \(a < b < c\), 'PEAK' if \(a < b\) and \(b > c\), and 'NONE' otherwise. If \(t\) is outside the specified range, the function skips the test case. After processing all test cases, the function does not return any value but prints the results for each test case.

