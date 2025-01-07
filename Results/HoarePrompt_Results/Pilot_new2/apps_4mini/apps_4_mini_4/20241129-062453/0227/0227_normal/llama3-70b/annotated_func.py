#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 23, and a is a list of n distinct positive integers where each integer a_k satisfies 1 ≤ a_k ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `m` is the count of distinct integers in `a` such that no element is double the previous one, `n` is the total number of elements in `a`, and `a` is a sorted list of `n` distinct positive integers. If `n` is 1, then `m` is 1.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function accepts a positive integer `n` (1 ≤ n ≤ 23) and a list `a` of `n` distinct positive integers (1 ≤ a_k ≤ 10^9). It counts how many distinct integers in `a` are such that no element is double the preceding element in the sorted list. If the count `m` is greater than 23, the function returns -1. Otherwise, it returns the count `m`.

