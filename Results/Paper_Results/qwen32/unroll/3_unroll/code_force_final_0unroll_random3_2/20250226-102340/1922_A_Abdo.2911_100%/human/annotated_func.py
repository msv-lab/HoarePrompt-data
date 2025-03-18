#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, for each test case n is an integer such that 1 ≤ n ≤ 20, and a, b, c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: The output state is a series of 'YES' or 'NO' printed for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function `func_1` processes a series of test cases, each consisting of three strings of equal length. For each test case, it determines if there exists at least one position where the third string differs from the first two strings, or if the third string matches at least one of the first two strings at every position. It prints 'YES' if such a condition is met for any test case, otherwise it prints 'NO'.

