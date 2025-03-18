#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2·10^5, p is a permutation of length n consisting of integers from 1 to n, and b is a sequence of n integers consisting only of 0s and 1s.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `b` is a list of integers obtained from the input split and converted to integers, `ans` is the count of elements in `b` where either `p[i] != i + 1` or `b[i] == 0`, and `i` is `n`.
    print(ans)
#Overall this is what the function does:The function `func()` accepts three parameters: `n`, `p`, and `b`. It reads these parameters from the user, where `n` is an integer indicating the length of permutations and sequences, `p` is a permutation of length `n` consisting of integers from 1 to `n`, and `b` is a sequence of `n` integers consisting only of 0s and 1s. The function calculates and returns the count of indices `i` (from 0 to `n-1`) where either `p[i]` is not equal to `i+1` or `b[i]` is equal to 0. The function handles the case where `n` is within the range \(1 \leq n \leq 2 \cdot 10^5\). If both `p[i]` and `b[i]` are valid and satisfy the condition `p[i] == i + 1` and `b[i] == 1`, such indices do not contribute to the final count. The function prints the calculated count at the end.

