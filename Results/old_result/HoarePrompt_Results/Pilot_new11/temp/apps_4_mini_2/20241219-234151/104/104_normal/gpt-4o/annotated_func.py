#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than 1, `a` is a list of `n` integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000; `max_erase` is the maximum number of consecutive integers that can be erased considering the gaps between the elements in `a`, `i` is `n - 1`.
    print(max_erase)
#Overall this is what the function does:The function reads a positive integer `n` (where 1 <= n <= 100) and a list `a` of `n` strictly increasing integers (where each integer is in the range 1 <= a[0] < a[1] < ... < a[n-1] <= 1000). It calculates the maximum number of consecutive integers that can be erased from between the elements of `a`, which is determined by finding the largest gap between consecutive integers in the list and subtracting 1 from that gap. After processing, the function prints this maximum value, `max_erase`. The function does not handle the case when `n` is equal to 1, which would lead to a potential error or undefined behavior since no gaps can exist in a single-element list. Additionally, the function does not validate the input, assuming it will always meet the specified constraints. The final state of the program is outputting the maximum number of consecutive integers that can be erased, represented by `max_erase`.

