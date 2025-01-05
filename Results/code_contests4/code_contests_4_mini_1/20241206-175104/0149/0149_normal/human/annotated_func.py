#State of the program right berfore the function call: n is an even integer such that 2 ≤ n ≤ 100, and a list of integers representing the initial positions of chess pieces, where each position is distinct and satisfies 1 ≤ pi ≤ n.
def func():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split(' ')))
    p = [(pi - 1) for pi in p]
    even = odd = 0
    for i in range(n / 2):
        even += abs(i * 2 - p[i])
        
        odd += abs(i * 2 + 1 - p[i])
        
    #State of the program after the  for loop has been executed: `n` is an even integer such that 2 ≤ `n` ≤ 100; `p` is a list of integers modified to be each element decremented by 1; `even` is the sum of `abs(i * 2 - p[i])` for `i` from 0 to `n/2 - 1`; `odd` is the sum of `abs(i * 2 + 1 - p[i])` for `i` from 0 to `n/2 - 1.
    print(min(even, odd))
#Overall this is what the function does:The function accepts an even integer `n` (where 2 ≤ n ≤ 100) and a list of distinct integers representing chess piece positions (1 ≤ pi ≤ n). It computes two sums: `even`, which represents the total distance of the pieces from their ideal positions if placed at even indices, and `odd`, which represents the total distance if placed at odd indices. The function then prints the minimum of these two sums, indicating the least total movement required to arrange the pieces either at even or odd indices.

