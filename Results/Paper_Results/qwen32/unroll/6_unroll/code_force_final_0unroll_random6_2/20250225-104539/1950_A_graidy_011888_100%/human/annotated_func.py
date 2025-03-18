#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000; for each of the t test cases, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9; n is an input integer. The loop has finished executing all n iterations, and for each iteration, it has printed either 'STAIR', 'PEAK', or 'NONE' based on the conditions provided. The values of t, a, b, c, and n remain unchanged.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b > c`, and 'NONE' otherwise. The function does not return any value; it only prints the results for each test case.

