#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100, `a` is a list of `n` integers such that 1 <= `a[0]` < `a[1]` < ... < `a[n-1]` <= 1000, `max_erase` is the maximum gap between consecutive elements in `a` minus one, which is `max(0, a[i] - a[i - 1] - 1)` for all valid `i`.
    print(max_erase)
#Overall this is what the function does:The function accepts an integer `n`, which specifies the number of elements in a list, and a list `a` of `n` integers that are sorted in strictly increasing order. It calculates the maximum gap between consecutive elements in the list, minus one, and prints this value. The function does not handle cases where `n` is 1, as there would be no gaps to compute, and it expects valid input according to the stated constraints.

