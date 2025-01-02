#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 2 ⋅ 10^{5}), representing the number of elements in the sequence. The second line contains n integers a_1, a_2, ..., a_n, where each a_i satisfies -10^{9} ≤ a_i ≤ 10^{9} and a_i ≠ 0.
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
    #State of the program after the if-else block has been executed: *`n` is the integer input by the user; `A` is a map object containing the integers from the input; `idx` is 0; `size` is `len(A)`; `total` is `size * (1 + size) / 2`; `p` is a list of `size` elements, with the first element being 1 or 0 and all others being 0; `q` is a list of `size` elements, with the first element being 0 or 1 and the rest being 0; the first element of `A` is greater than 0 or less than or equal to 0
    for i in xrange(1, size):
        if A[i] > 0:
            p[i] = p[i - 1] + 1
            q[i] = q[i - 1]
        else:
            p[i] = q[i - 1]
            q[i] = p[i - 1] + 1
        
    #State of the program after the  for loop has been executed: Output State: **`i` is `size`, `size` is a positive integer, `idx` is `size - 1`, `total` is `size * (1 + size) / 2`, `p` and `q` lists are updated such that for every index `j` from `1` to `size - 1`:
    #- If `A[j] > 0`, then `p[j] = p[j - 1] + 1` and `q[j] = q[j - 1]`.
    #- If `A[j] <= 0`, then `p[j] = q[j - 1]` and `q[j] = p[j - 1] + 1`.
    #
    #The first element of `A` remains unchanged and is greater than 0 or less than or equal to 0. The lists `p` and `q` are initialized such that `p[0]` is 1 or 0 and all other elements of `p` are 0, while `q[0]` is 0 or 1 and all other elements of `q` are 0. If the loop does not execute at all (i.e., `size` is 1), then `p` and `q` are `[1]` and `[0]`, respectively, and the first element of `A` is greater than 0 or less than or equal to 0.
    print('%s %s' % (sum(q), sum(p)))
#Overall this is what the function does:The function accepts an integer `n` representing the number of elements in a sequence, followed by `n` integers `a_1, a_2, ..., a_n` where each integer satisfies \(-10^9 \leq a_i \leq 10^9\) and \(a_i \neq 0\). It then constructs two lists, `p` and `q`, where for each index \(j\) from 1 to \(n-1\):

- If \(A[j] > 0\), then \(p[j] = p[j - 1] + 1\) and \(q[j] = q[j - 1]\).
- If \(A[j] \leq 0\), then \(p[j] = q[j - 1]\) and \(q[j] = p[j - 1] + 1\).

The initial values of `p[0]` and `q[0]` are set based on whether \(A[0] > 0\) or \(A[0] \leq 0\). After constructing these lists, the function prints the sum of the elements in `q` and `p`.

