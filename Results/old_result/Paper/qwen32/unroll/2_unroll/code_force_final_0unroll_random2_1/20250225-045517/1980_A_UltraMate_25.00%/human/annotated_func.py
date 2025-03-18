#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and m are integers such that 1 ≤ n ≤ 50 and 1 ≤ m ≤ 5. a is a string of length n consisting of characters from 'A' to 'G'.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        s = input()
        
        ans = 0
        
        p = 'ABCDEF'
        
        hmp = Counter(s)
        
        for i in p:
            if i not in hmp:
                ans += m
        
        for i in hmp:
            if hmp[i] < m:
                ans += m - hmp[i]
        
        print(ans)
        
    #State: `t` remains the same, `n`, `m`, and `a` remain unchanged, and `ans` is printed `t` times with values dependent on the input for each iteration.
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n` and `m`, and a string `a` of length `n`. For each test case, it calculates and prints the minimum number of changes required to ensure that each character from 'A' to 'F' appears at least `m` times in the string `a`. Characters 'G' and any missing characters from 'A' to 'F' are not considered in the count.

