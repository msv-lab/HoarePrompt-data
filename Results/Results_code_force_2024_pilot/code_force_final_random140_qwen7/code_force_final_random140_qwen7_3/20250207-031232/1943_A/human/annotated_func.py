#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where 0 ≤ a_i < n. Additionally, the sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: Output State: After all iterations of the loop have finished, the variable `cntl` will be a list of length `n + 1` where each element `cntl[i]` represents the number of times the index `i` appears in the list `a` across all test cases. The variable `c` will always be 0 because it is reset to 2 at the beginning of each iteration and is only decremented when `cntl[j]` is less than 2 but not zero. The loop will continue to check the condition `if cntl[0] == 0` and if so, it will print 0. Otherwise, it will find the smallest index `j` (starting from 1) where `cntl[j]` is less than 2 and print `j`. If no such `j` exists, it will print `n`.
    #
    #In natural language: After all iterations of the loop, `cntl` will contain the total count of each index from 0 to `n` across all lists `a` provided as input. The variable `c` will be 0 after each iteration. The loop will print the smallest index `j` (starting from 1) where the count of `j` in `a` is less than 2, or it will print 0 if `cntl[0]` is still 0 after processing all inputs, or it will print `n` if no such `j` is found.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `n` and a list `a` of `n` non-negative integers. For each test case, it calculates the frequency of each index from 0 to `n` in the list `a`. It then determines and prints the smallest index `j` (starting from 1) where the count of `j` in `a` is less than 2. If `cntl[0]` is still 0 after processing all inputs, it prints 0. If no such `j` is found, it prints `n`. The function does not return any value but outputs the result for each test case.

