#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 23, and a is a list of n distinct positive integers where each integer a_k satisfies 1 ≤ a_k ≤ 10^9.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1
    for i in range(1, n):
        if a[i] != a[i - 1] * 2:
            m += 1
        
    #State of the program after the  for loop has been executed: `m` is equal to the count of elements in `a` that are not double the previous element, `n` is a positive integer such that 1 ≤ n ≤ 23, and `a` is a sorted list of `n` distinct positive integers. If `n` is 1, then `m` is 1.
    print(m if m <= 23 else -1)
#Overall this is what the function does:The function accepts a positive integer `n` representing the count of distinct positive integers and a list `a` of `n` distinct positive integers. It counts how many elements in the sorted list `a` are not double the previous element and returns this count if it is less than or equal to 23; otherwise, it returns -1. If `n` is 1, the function will always return 1 since there are no previous elements to compare.

