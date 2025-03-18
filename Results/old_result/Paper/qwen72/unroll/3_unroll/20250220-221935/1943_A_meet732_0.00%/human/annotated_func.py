#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, n is an integer where 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop reads `t` test cases, and for each test case, it reads `n` and a list `a` of `n` integers. It then counts the occurrences of each integer in `a` using the list `cntl`. If `cntl[0]` is 0, it prints 0. Otherwise, it initializes `c` to the minimum of 2 and `cntl[0]`, and iterates through `cntl` from index 1 to `n`. It decrements `c` for each index `j` where `cntl[j]` is less than 2. If `c` reaches 0 or `j` reaches `n`, it prints `j` and breaks out of the loop. The values of `t`, `n`, and `a` remain unchanged, but `cntl` and `c` are modified during the loop execution.
#Overall this is what the function does:The function reads `t` test cases from the input, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it counts the occurrences of each integer in `a` and determines a value to print based on these counts. If the integer 0 does not appear in `a`, it prints 0. Otherwise, it finds the smallest index `j` such that the count of `j` in `a` is less than 2, and prints this index. If no such index is found, it prints `n`. The function does not return any value; it only prints the results. The input variables `t`, `n`, and `a` are not modified by the function.

