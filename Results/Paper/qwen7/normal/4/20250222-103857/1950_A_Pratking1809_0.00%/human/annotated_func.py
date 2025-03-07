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
        
    #State: Output State: `t` is an integer such that \(1 \leq t \leq 1000\), `q` is the total number of iterations the loop has executed, `mn` is 100, `a` is the first input integer, `b` is the second input integer, `c` is the third input integer, and the loop has completed all its iterations. The values of `a`, `b`, and `c` from the last iteration of the loop are the most recent inputs provided, and the loop has printed 'STAIR' if `a < b < c` and 'PEAK' if `a < b > c` for those inputs. If neither condition is met, it printed 'NONE'.
#Overall this is what the function does:The function processes `q` sets of three integers (`a`, `b`, `c`) within the range 0 to 9. For each set, it checks if `a < b < c` and prints 'STAIR', if `a < b > c` and prints 'PEAK'. If neither condition is met, it prints 'NONE'. After processing all sets, the function does not return any value but prints the results for each set.

