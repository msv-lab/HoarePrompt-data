#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        possible = False
        
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        
        if possible:
            print('YES')
        else:
            print('NO')
        
    #State: Output State: t is an integer between 1 and 1000 (inclusive), n, a, b, c are strings of equal length n, and after executing the loop, each line of output consists of either 'YES' or 'NO' based on the conditions inside the loop.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `t` (1 ≤ t ≤ 1000), an integer `n` (1 ≤ n ≤ 20), and three strings `a`, `b`, and `c` each consisting of exactly `n` lowercase Latin letters. For each test case, it checks if it's possible to rearrange the characters of string `c` such that no position has the same character as in `a` or `b`. If such a rearrangement is possible, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results for each test case.

