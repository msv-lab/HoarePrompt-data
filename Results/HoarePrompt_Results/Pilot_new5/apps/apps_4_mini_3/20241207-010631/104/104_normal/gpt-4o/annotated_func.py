#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, and a is a list of n integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
def func():
    n = int(input())
    a = list(map(int, input().split()))
    max_erase = 0
    for i in range(1, n):
        max_erase = max(max_erase, a[i] - a[i - 1] - 1)
        
    #State of the program after the  for loop has been executed: `max_erase` is the maximum gap between consecutive integers in `a` minus 1, `n` is an integer between 1 and 100, `a` is a list of `n` integers where 1 <= a[0] < a[1] < ... < a[n-1] <= 1000.
    print(max_erase)
#Overall this is what the function does:The function accepts an integer `n` (where 1 <= n <= 100) and a list `a` containing `n` strictly increasing integers (where each integer satisfies 1 <= a[0] < a[1] < ... < a[n-1] <= 1000). It calculates the maximum gap between consecutive integers in `a` minus one and prints this value. If `n` is 1, the function will output 0 since there are no gaps to compute.

