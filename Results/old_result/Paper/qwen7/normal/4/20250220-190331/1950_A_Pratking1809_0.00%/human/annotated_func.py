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
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 1000\), `q` is a positive integer, `i` is 3, `a`, `b`, and `c` are integers input by the user. If `a < b < c`, the condition remains unchanged; otherwise, the conditions `a < b > c` or `b` is not greater than `c` hold true for each iteration of the loop. The variable `mn` remains 100 as it is not affected by the loop.
    #
    #This means after the loop has executed all its iterations, `t` will still be within the range of 1 to 1000, `q` will be a positive integer indicating the number of iterations, `i` will be equal to `q` (the total number of iterations), and `a`, `b`, and `c` will be the last set of integers input by the user during the final iteration of the loop. The variable `mn` will remain unchanged at 100 since it is not involved in any operations within the loop.
#Overall this is what the function does:The function reads multiple sets of three integers (a, b, c) from the user, each set within the range 0 to 9. For each set, it checks if a < b < c, in which case it prints 'STAIR'. If a < b > c, it prints 'PEAK'. Otherwise, it prints 'NONE'. After processing all sets, the function does not return anything (None).

