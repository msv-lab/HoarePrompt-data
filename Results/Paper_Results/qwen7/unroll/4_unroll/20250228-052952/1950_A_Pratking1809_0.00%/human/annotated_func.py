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
        
    #State: The output state will consist of q lines, each containing either 'STAIR', 'PEAK', or 'NONE' based on the conditions evaluated for the input values (a, b, c) in each iteration of the loop. The specific content of each line depends on the input provided during each iteration.
#Overall this is what the function does:The function processes `q` test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it determines whether the sequence `a, b, c` represents a 'STAIR' (where `a < b < c`) or a 'PEAK' (where `a < b > c`), and prints the corresponding label. If neither condition is met, it prints 'NONE'. After processing all test cases, the function outputs `q` lines, each containing either 'STAIR', 'PEAK', or 'NONE' based on the conditions evaluated for the input values in each iteration.

