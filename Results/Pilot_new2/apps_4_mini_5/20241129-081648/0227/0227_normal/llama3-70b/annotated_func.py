#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 23, and a is a list of n distinct positive integers where each integer is in the range 1 ≤ a[k] ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `n` is an input positive integer such that 1 ≤ `n` ≤ 23, `a` is a sorted list of `n` distinct positive integers, `m` is the count of elements where `a[i]` is not equal to `a[i - 1] * 2` plus 1, and the loop executed `n - 1` times.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 23) and a list `a` of `n` distinct positive integers (1 ≤ a[k] ≤ 10^9). It counts how many elements in the sorted list `a` are not equal to double the previous element, initialized with a count of 1. Finally, it prints this count `m`, but if `m` exceeds 23, it prints -1 instead. The function does not return any value.

