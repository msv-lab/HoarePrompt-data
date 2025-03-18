#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 2 <= n <= 2 \cdot 10^5, and for each test case, the grid is a 2 \times n grid where each cell contains either 0 or 1.
def func():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input().strip()
        
        b = input().strip()
        
        ans = ''
        
        i = 0
        
        work = True
        
        while i < len(a):
            if work:
                ans += a[i]
                if i + 1 < len(a) and b[i] < a[i + 1]:
                    work = False
                elif i + 1 == len(a):
                    ans += b[i]
                    break
                else:
                    i += 1
            else:
                ans += b[i]
                i += 1
        
        print(ans)
        
        counter = 1
        
        for j in range(len(a) - 1):
            if a[j + 1] == b[j]:
                counter += 1
            elif a[j + 1] == '0' and b[j] == '1':
                counter = 1
            else:
                break
        
        print(counter)
        
    #State: The loop has completed all `t` iterations. For each iteration, `n` was an input integer such that 2 <= n <= 2 \cdot 10^5, `a` and `b` were non-empty strings containing the input provided by the user, stripped of leading and trailing whitespace, and must have had at least 2 characters. `ans` is a string that contains characters from `a` and `b` based on the conditions in the loop, `i` is equal to the length of `a` for each iteration, `work` is either True or False depending on the last iteration's conditions, `j` is `len(a) - 2`, and `counter` is the number of consecutive characters from `a[1]` to `a[len(a) - 1]` that match the corresponding characters in `b` from `b[0]` to `b[len(a) - 2]`, or 1 if the loop was reset due to a '0' in `a` and a '1' in `b` at any point, or the loop was broken if any character in `a` from `a[1]` to `a[len(a) - 1]` did not match the corresponding character in `b` from `b[0]` to `b[len(a) - 2]` and was not a '0' followed by a '1'.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of an integer `n` and two strings `a` and `b` representing a 2xN grid. For each test case, it constructs a string `ans` by alternating characters from `a` and `b` based on certain conditions and prints this string. It also calculates a `counter` that tracks the number of consecutive matching characters between `a` and `b` from the second character of `a` to the second-to-last character of `b`, or resets to 1 if a specific pattern is encountered, and prints this counter. After processing all test cases, the function completes and the final state is that all test cases have been processed and their results printed.

