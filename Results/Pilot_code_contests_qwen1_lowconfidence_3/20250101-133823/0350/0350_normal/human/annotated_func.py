#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 2 ⋅ 10^{5}) representing the number of elements in the sequence, and the second line contains n integers a_1, a_2, ..., a_n (-10^{9} ≤ a_i ≤ 10^{9}; a_i ≠ 0) representing the elements of the sequence.
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
    #State of the program after the if-else block has been executed: *`n` is an integer (1 ≤ n ≤ 2 ⋅ 10^{5}), `A` is a map object of integers, `idx` is 0, `size` is `len(A)`, `total` is `size * (1 + size) / 2`, `p` is a list of `size` zeros, `q` is a list of `size` zeros. If `A[0] > 0`, then `p[0]` is 1 and `q[0]` is 0. If `A[0] ≤ 0`, then `q[0]` is 1 and `p[0]` is 0.
    for i in xrange(1, size):
        if A[i] > 0:
            p[i] = p[i - 1] + 1
            q[i] = q[i - 1]
        else:
            p[i] = q[i - 1]
            q[i] = p[i - 1] + 1
        
    #State of the program after the  for loop has been executed: `size` is the length of the list `A`, `p[i]` is the count of positive elements in `A` up to index `i` plus the initial value `p[0]`, and `q[i]` is the count of non-positive elements in `A` up to index `i` plus the initial value `q[0]`.
    print('%s %s' % (sum(q), sum(p)))
#Overall this is what the function does:The function processes a sequence of integers provided through standard input. It reads the number of elements `n` and the sequence itself, then calculates the cumulative counts of positive and non-positive elements up to each index in the sequence. Specifically, it maintains two arrays `p` and `q`, where `p[i]` represents the count of positive elements in the sequence up to index `i` including the initial value, and `q[i]` represents the count of non-positive elements up to index `i` including the initial value. After processing, the function prints the total count of non-positive elements and the total count of positive elements in the sequence. Potential edge cases include the sequence having only one element, which would initialize both `p[0]` and `q[0]` to either 1 or 0 depending on the sign of the first element. Missing functionality includes handling empty input sequences, although the provided code does not explicitly handle this case; it assumes `n` is always greater than zero.

