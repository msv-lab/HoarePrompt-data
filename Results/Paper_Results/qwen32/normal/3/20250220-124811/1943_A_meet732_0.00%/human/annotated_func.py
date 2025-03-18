#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4) — the number of test cases. Each test case consists of two lines: the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5), and the second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n). The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: the sequence of outputs from each test case, printed during the loop execution.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers (each between 0 and `n-1`). For each test case, it determines and prints a specific integer based on the frequency of elements in the list.

