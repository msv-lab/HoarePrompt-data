#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 2 · 10^5) followed by two binary strings of length n, representing the top and bottom rows of the grid, respectively. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` test cases have been processed, each with its own `n`, `a`, `b`, `ans`, and `counter` values printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and two binary strings of length `n`. For each test case, it constructs a new string `ans` by selectively choosing characters from the top and bottom strings based on specific conditions. It then prints the constructed string `ans` and a counter value representing the length of the longest prefix of the top string that matches a suffix of the bottom string under certain conditions.

