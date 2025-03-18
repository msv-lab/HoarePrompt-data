#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: After the loop executes all iterations, the list `cntl` will contain the frequency of each number appearing in the list `a`. Specifically, for each index `i` in `a`, the value at `cntl[i]` will be the number of times `i` appears in `a`. All other elements in `cntl` (those indices not present in `a`) will remain as 0. Additionally, if `cntl[0]` is 0, the loop will check if `j` equals `n` and `cntl[j]` is less than 2 for all `j` from 1 to `n`. If these conditions are met, the loop will break, and the smallest `j` satisfying the condition will be printed. If `cntl[0]` is not 0, the loop will also break when `j` equals `n`, and no value will be printed since `c` will be 0.
    #
    #In summary, `cntl` will reflect the frequency of each element in `a`, and the loop will either print the smallest `j` for which `cntl[j]` is less than 2 (excluding 0), or it will not print anything if no such `j` exists.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( n \) and a list \( a \) of \( n \) non-negative integers. For each test case, it constructs a frequency count of the numbers in the list \( a \) using the `cntl` list. It then checks if any number in \( a \) appears fewer than 2 times (excluding zero). If such a number exists, it prints the smallest one; otherwise, it prints nothing.

