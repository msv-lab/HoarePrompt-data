#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 23, and the sequence a consists of n distinct integers where each integer a_k satisfies 1 <= a_k <= 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= `n` <= 23, `m` is the count of integers in `a` that do not satisfy the condition `a[i] == a[i - 1] * 2` for `i` from 1 to `n-1`. `a` is a sorted list of `n` distinct integers satisfying 1 <= `a_k` <= 10^9. If the loop does not execute (when `n` is 1), `m` remains 1.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function accepts a positive integer `n` from user input, representing the number of distinct integers to be processed. It then reads `n` integers, sorts them, and counts how many integers do not satisfy the condition that each element is double the previous one. The function returns this count `m`, unless `m` exceeds 23, in which case it returns -1. If there is only one integer (when `n` is 1), the function will return 1 as there are no comparisons to make. The function does not handle input validation for the constraints provided, so inappropriate inputs could lead to unexpected behavior.

