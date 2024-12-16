#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^5, p is a permutation of integers from 1 to n, and b is a sequence of n integers consisting only of 0s and 1s.
def func():
    n = int(input())
    p = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] != i + 1:
            ans += 1
        
        if b[i] == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 2 \times 10^5\), `ans` is the count of indices `i` where either `p[i] != i + 1` or `b[i] == 0`.
    print(ans)
#Overall this is what the function does:The function reads three inputs `n`, `p`, and `b` and returns the count of indices where the permutation `p` is not in its natural order (i.e., `p[i] != i + 1`) or the sequence `b` contains a 0.

