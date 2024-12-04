#State of the program right berfore the function call: n and k are integers such that 1 ≤ n, k ≤ 10^18 and k ≤ n.
def func():
    n, k = map(int, input().split())
    if ((n - 1) // k > n // k) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` and `k` are integers, satisfying 1 ≤ n, k ≤ 10^18 and k ≤ n. If the condition (n - 1) // k > n // k holds true, the program outputs 'YES'. Otherwise, it outputs 'NO'.
#Overall this is what the function does:The function accepts two integer parameters, `n` and `k`, with the constraints that 1 ≤ n, k ≤ 10^18 and k ≤ n. It checks whether the integer division of `n - 1` by `k` is greater than the integer division of `n` by `k`. If the condition holds true, it outputs 'YES'; otherwise, it outputs 'NO'. The function does not return any value; it only prints the result.

