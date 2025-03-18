#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000, and for each test case, n is an integer such that 2 <= n <= 50, and p is a list of integers of length n where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: t is an integer such that 1 <= t <= 5000, and for each test case, n is an integer such that 2 <= n <= 50, and p is a list of integers of length n where 1 <= p_i <= n, p_i ≠ i, and all p_i are distinct. The loop has printed either 2 or 3 for each test case, depending on whether a pair (i, p) was found such that l[p - 1] == i + 1.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` and a list of integers `p` of length `n`. For each test case, it checks if there exists an index `i` such that `p[p[i] - 1] == i + 1`. If such an index is found, the function prints `2` and moves to the next test case. If no such index is found, it prints `3`. After processing all test cases, the function concludes.

