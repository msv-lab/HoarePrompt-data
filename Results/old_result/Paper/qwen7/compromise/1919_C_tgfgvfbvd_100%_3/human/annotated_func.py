#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: Output State: After the loop executes all the iterations, `x` will be equal to `n-1`, `a` will be the minimum value found in the list `l`, `b` will be the second smallest value found in the list `l`, and `c` will be the count of elements in `l` that are strictly greater than `b`. The variable `n` remains unchanged, and `l` will contain the original list of integers entered by the user.
    #
    #In more detail:
    #- `x` will be `n-1` because the loop iterates from `0` to `n-1`.
    #- `a` will hold the minimum value from the list `l` because any value less than or equal to `a` replaces `a`, and `a` is set to `b` when `a` is not greater than `b`.
    #- `b` will hold the second smallest value from the list `l` because it is updated only when `l[x]` is between `a` and `b`.
    #- `c` will count how many times `a` is replaced by `l[x]` (i.e., how many elements are strictly greater than `b`), which happens whenever `l[x]` is greater than `b`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. For each test case, it finds the second smallest element in the list and counts how many elements are strictly greater than this second smallest element. It then prints the count for each test case.

