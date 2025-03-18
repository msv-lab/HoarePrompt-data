#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 2 · 10^5, and a list of integers a of length n where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: the outputs for each test case concatenated together, with each output corresponding to the smallest index j as described above for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of integers `a` of length `n`. For each test case, it determines and prints the smallest index `j` such that there are fewer than two occurrences of any index from `0` to `j` in the list `a`. If all indices from `0` to `n` have at least two occurrences, it prints `n`.

