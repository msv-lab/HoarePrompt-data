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
        
    #State: `t` is an integer such that \(1 \leq t \leq 1000\), `q` is the total number of inputs provided by the user, `i` is equal to `q`, `a`, `b`, and `c` are the last set of integers entered by the user, and the output consists of `q` lines each indicating whether the input triplet forms a 'STAIR', 'PEAK', or 'NONE' based on the conditions given.
#Overall this is what the function does:The function processes `q` sets of three integers (a, b, c) where each integer is between 0 and 9 inclusive. For each set, it checks if the integers form a 'STAIR' (a < b < c) or a 'PEAK' (a < b > c) pattern. If neither condition is met, it outputs 'NONE'. The function prints one line for each set of integers processed, indicating whether the pattern is 'STAIR', 'PEAK', or 'NONE'. After processing all sets, the function concludes without returning any value.

