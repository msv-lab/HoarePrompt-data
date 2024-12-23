#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a[i] satisfies -100 ≤ a[i] ≤ 100.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b, c = 0, 0
    for i in range(n):
        if i % 2 == 0:
            b += a[i]
        else:
            c += a[i]
        
    #State of the program after the  for loop has been executed: `b` is the sum of `a[i]` for even `i` from `0` to `n-1`, `c` is the sum of `a[i]` for odd `i` from `0` to `n-1`, `a` is a sorted list of `n` integers in descending order satisfying -100 ≤ `a[i]` ≤ 100, and `n` is an integer within the range 1 ≤ `n` ≤ 100.
    print(b - c)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list `a` of `n` integers (each satisfying -100 ≤ a[i] ≤ 100). It sorts the list `a` in descending order and calculates two sums: `b`, which is the sum of the integers at even indices, and `c`, which is the sum of the integers at odd indices within the sorted list. Finally, it prints the difference `b - c`. The function does not handle invalid inputs or provide output for cases where `n` does not meet specified constraints.

