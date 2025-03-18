#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, representing the number of test cases. Each test case consists of an integer n where 1 ≤ n ≤ 2 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
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
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break
        
    #State: The loop has completed all its iterations. For each test case, `n` is an input integer greater than 0, `a` is a list of integers read from input, and `cntl` is a list of length `n + 1` where each element at index `i` in `cntl` represents the count of how many times the integer `i` appears in `a`. If `cntl[0]` is 0, the output is 0. Otherwise, the output is the smallest integer `j` between 1 and `n` such that `cntl[j]` is 0 or `cntl[j]` is less than 2, and `c` is 0. If no such `j` exists, no value is printed for that test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and a list of `n` integers. It reads the number of test cases `t` (where `1 ≤ t ≤ 2 · 10^4`) and for each test case, it reads `n` (where `1 ≤ n ≤ 2 · 10^5`) and a list of `n` integers `a` (where `0 ≤ a_i < n`). The function then counts the occurrences of each integer in `a` and stores these counts in a list `cntl` of length `n + 1`. If the count of `0` in `a` is zero, the function prints `0`. Otherwise, it prints the smallest integer `j` between `1` and `n` such that the count of `j` in `a` is either `0` or less than `2`, and the count of `0` in `a` is at least `2`. If no such `j` exists, no value is printed for that test case. After processing all test cases, the function completes and the program state reflects the printed outputs for each test case.

