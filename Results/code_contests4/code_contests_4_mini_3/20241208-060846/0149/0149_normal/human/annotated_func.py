#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 100, and positions is a list of distinct integers where 1 ≤ pi ≤ n.
def func():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    p = [(pi - 1) for pi in p]
    even = odd = 0
    for i in range(n / 2):
        even += abs(i * 2 - p[i])
        
        odd += abs(i * 2 + 1 - p[i])
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 ≤ `n` ≤ 100; `p` is a list of integers with each element decreased by 1; `even` is the sum of `abs(i * 2 - p[i])` for `i` from `0` to `n/2 - 1`; `odd` is the sum of `abs(i * 2 + 1 - p[i])` for `i` from `0` to `n/2 - 1.
    print(min(even, odd))
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 100) and a list of distinct integers `p` (where each integer is in the range 1 ≤ pi ≤ n). It calculates two sums: `even`, which is the total distance of each adjusted position at even indices from their expected positions, and `odd`, which is the total distance for odd indices. The function then prints the minimum of these two sums. However, it does not handle cases where `p` contains integers outside the specified range or where `n` is not exactly even, even though the precondition states that `n` will always be even.

