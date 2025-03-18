#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n is a positive integer such that 1 ≤ n ≤ 100. a is a list of n integers sorted in non-decreasing order, where 1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9. b is a list of n integers sorted in non-decreasing order, where 1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: Output State: After the loop executes all iterations, `cnt` will be the total count of elements in `b` that are less than `a[i]` for all iterations. `i` will be equal to `n`, `j` will be `-1`, `n` will remain unchanged, and `t` will be 0 since all iterations have been completed. `a` and `b` will be lists of integers obtained from the input as specified in the loop body.
    #
    #In natural language, after the loop completes all its iterations, `cnt` will hold the cumulative count of elements in `b` that were found to be less than the corresponding element in `a` starting from the first element of `a` and moving rightwards through the list. The variable `i` will be set to `n` indicating the end of the list `a`, `j` will be set to `-1` as it is decremented from `n-1` until it reaches `-1`, `n` will stay the same as it was initialized, and `t` will be 0 because all iterations have been executed. The lists `a` and `b` will retain their values as they were input during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two lists of integers, `a` and `b`, both sorted in non-decreasing order. It then counts and prints the number of elements in `b` that are less than the corresponding elements in `a`. After processing all test cases, it outputs the total count of such elements across all test cases.

