#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 2 ⋅ 10^{5}, and a is a list of n integers where each integer a_i satisfies -10^{9} ≤ a_i ≤ 10^{9} and a_i ≠ 0.
def func():
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    n = int(raw_input())
    A = map(int, input().split())
    idx, size = 0, len(A)
    total = size * (1 + size) / 2
    p = [0] * size
    q = [0] * size
    if (A[0] > 0) :
        p[0], q[0] = 1, 0
    else :
        q[0], p[0] = 1, 0
    #State of the program after the if-else block has been executed: *`n` is an integer input from the user where 1 ≤ n ≤ 2 ⋅ 10^5, `a` is a list of `n` integers where each integer `a_i` satisfies -10^9 ≤ a_i ≤ 10^9 and a_i ≠ 0, `input` is assigned the function `sys.stdin.readline`, recursion limit is set to 10^6, `A` is a map object containing integers read from the input, `idx` is 0, `size` is the length of the map object `A`, `total` is `size * (1 + size) / 2`, `p` is a list of `size` zeros, and `q` is a list of `size` zeros. If `A[0] > 0`, then `p[0] = 1` and `q[0] = 0`. Otherwise, if `A[0] <= 0`, then `p[0] = 0` and `q[0] = 1`.
    for i in xrange(1, size):
        if A[i] > 0:
            p[i] = p[i - 1] + 1
            q[i] = q[i - 1]
        else:
            p[i] = q[i - 1]
            q[i] = p[i - 1] + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer input from the user where \(1 \leq n \leq 2 \cdot 10^5\), `a` is a list of `n` integers where each integer \(a_i\) satisfies \(-10^9 \leq a_i \leq 10^9\) and \(a_i \neq 0\), `input` is assigned the function `sys.stdin.readline`, `A` is a map object containing integers read from the input, `idx` is 0, `size` is the length of the map object `A` and must be at least 1, `total` is `size * (1 + size) / 2`, `p` is a list of `size` elements, `q` is a list of `size` elements, `i` is `size`. For each index \(i\) in the range \(1 \leq i < size\), if \(A[i] > 0\), then \(p[i] = p[i-1] + 1\) and \(q[i] = q[i-1]\). Otherwise, if \(A[i] \leq 0\), then \(p[i] = q[i-1]\) and \(q[i] = p[i-1] + 1\).
    print('%s %s' % (sum(q), sum(p)))
#Overall this is what the function does:The function reads an integer `n` and a list `A` of `n` integers from standard input, where each integer in `A` satisfies -10^9 ≤ a_i ≤ 10^9 and a_i ≠ 0. It then processes the list `A` to compute two values: the sum of the number of negative-to-positive transitions and the sum of the number of positive-to-negative transitions in the list. These two values are printed as a pair of integers. The function does not return any value but instead prints the result directly. Edge cases include handling lists of length 1, where no transitions can occur, and ensuring that the initial state of `p[0]` and `q[0]` is correctly set based on the sign of the first element in `A`.

