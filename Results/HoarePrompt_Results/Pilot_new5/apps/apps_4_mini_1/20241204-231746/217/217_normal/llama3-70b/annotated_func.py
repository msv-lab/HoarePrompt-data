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
        
    #State of the program after the  for loop has been executed: `b` is the sum of the elements at even indices of `a`, `c` is the sum of the elements at odd indices of `a`, `n` is the length of `a`, and `a` is a list of integers sorted in descending order satisfying -100 ≤ a[i] ≤ 100. If `n` is 0, then both `b` and `c` will be 0.
    print(b - c)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (each satisfying -100 ≤ a[i] ≤ 100). It sorts the list `a` in descending order and calculates the difference between the sum of integers at even indices and the sum of integers at odd indices in the sorted list. It then prints this difference.

