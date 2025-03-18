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
        
    #State: Output State: The `cntl` list will contain the count of how many times each integer from the input list `a` appeared across all iterations. Specifically, for each integer `i` in `a`, `cntl[i]` will hold the total frequency of `i` appearing in `a` for all test cases. The value at index 0 of `cntl` will always be 0 because no input specifies any operations that would modify it otherwise. The variable `c` will be set to the minimum of 2 and the initial count of 0s in `a`, minus the number of iterations where `j` was incremented without breaking the inner loop. The variable `j` will hold the smallest index `i` (greater than 0) where `cntl[i]` is less than 2, or `n` if no such index exists. If no such index is found, the loop will break when `c` reaches 0 or `j` equals `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( n \) and a list \( a \) of \( n \) non-negative integers. For each test case, it calculates the frequency of each integer in the list \( a \) and determines the smallest index \( i \) (greater than 0) where the frequency of \( i \) is less than 2. If no such index exists, it prints \( n \). The function outputs the result for each test case.

