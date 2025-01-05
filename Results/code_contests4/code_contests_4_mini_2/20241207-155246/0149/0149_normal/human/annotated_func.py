#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 100, and positions is a list of distinct integers (1 ≤ pi ≤ n) representing the initial positions of the chess pieces.
def func():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    p = [(pi - 1) for pi in p]
    even = odd = 0
    for i in range(n / 2):
        even += abs(i * 2 - p[i])
        
        odd += abs(i * 2 + 1 - p[i])
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 2 and 100; `even` is the sum of `abs(i * 2 - p[i])` for `i` from 0 to `n // 2 - 1`; `odd` is the sum of `abs(i * 2 + 1 - p[i])` for `i` from 0 to `n // 2 - 1; `p` is a list of distinct integers (1 ≤ `pi` ≤ `n`).
    print(min(even, odd))
#Overall this is what the function does:The function accepts an even integer `n` (2 ≤ n ≤ 100) and a list of distinct integers `p` (1 ≤ pi ≤ n) representing the initial positions of chess pieces. It calculates two sums: `even`, which is the total of absolute differences between the expected even positions and the actual positions, and `odd`, which is the total of absolute differences between the expected odd positions and the actual positions. The function then prints the minimum of these two sums, representing the least total movement required to rearrange the chess pieces to either all even or all odd positions.

