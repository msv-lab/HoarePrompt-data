#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n is a positive integer such that 1 ≤ n ≤ 100. a and b are arrays of length n, where a and b are sorted in non-decreasing order, and 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9 for all i.
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
        
    #State: Output State: `cnt` is a non-negative integer, `n` is a positive integer, `a` is a list of integers, `b` is a list of integers, `i` is either `n` or the last value it reached during the loop execution, `j` is `n - 1`.
    #
    #Explanation: After the loop executes all its iterations, the variable `i` will be equal to `n` because the loop increments `i` until it reaches `n`. The variable `j` will be equal to `n-1` because the loop runs through `range(n)`, meaning `j` will iterate from 0 to `n-1`. The value of `cnt` will be the total count of times `b[j]` was found to be less than `a[i]` during the loop execution for all iterations of the outer loop. Since the outer loop runs `t` times, `cnt` will accumulate the counts from each iteration, resulting in a non-negative integer value.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it compares two sorted arrays `a` and `b` of length `n`. It counts the number of times an element in array `b` is less than the corresponding element in array `a`. The function prints this count for each test case and does not return any value.

