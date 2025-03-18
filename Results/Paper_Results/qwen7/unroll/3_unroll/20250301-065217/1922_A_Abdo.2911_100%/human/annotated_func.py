#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20. a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: Output State: The output state consists of 'YES' or 'NO' printed for each iteration based on the conditions inside the loop. For each input 'n', strings 'a', 'b', and 'c' are compared character by character. If any character in 'c' does not match either 'a' or 'b' at the same position where 'a' and 'b' match, 'possible' is set to True and 'YES' is printed. Otherwise, if 'c' contains characters that do not conflict with 'a' or 'b', 'NO' is printed. This process repeats 't' times, where 't' is the first input integer.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 1000), followed by an integer `n` (1 ≤ n ≤ 20) and three strings `a`, `b`, and `c` (each consisting of exactly `n` lowercase Latin letters). For each test case, it checks if string `c` can be formed by swapping characters between strings `a` and `b` at the same positions where `a` and `b` have matching characters. If such swaps are possible, it prints 'YES'; otherwise, it prints 'NO'. This process is repeated `t` times.

