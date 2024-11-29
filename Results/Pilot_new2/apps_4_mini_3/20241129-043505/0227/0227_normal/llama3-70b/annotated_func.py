#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 23, and a is a list of n distinct positive integers, where each integer a[k] satisfies 1 ≤ a[k] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: - If the list `a` has `n` elements, then `m` can be at most `n`, as every distinct positive integer could potentially create a case where `a[i]` does not equal `a[i - 1] * 2`.
    #- The minimum value of `m` will be 1, and the maximum value will be `n` depending on the entries in the sorted list `a`.
    #
    #Thus, we can summarize the final output state as follows:
    #
    #Output State:
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of `n` distinct integers. It counts how many distinct groups of integers exist in `a` such that each integer is not twice the previous integer. If the count exceeds 23, it returns -1; otherwise, it returns the count. It does not validate inputs and may fail if inputs are outside expected ranges.

