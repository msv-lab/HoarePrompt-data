#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n, k ≤ 10^18 and k ≤ n.
def func():
    n, k = map(int, input().split())
    if (n // k % 2 == 1) :
        print('YES')
    else :
        print('NO')
    #State of the program after the if-else block has been executed: *`n` is an input positive integer such that \( 1 \leq n \leq 10^{18} \) and `k` is an input positive integer such that \( 1 \leq k \leq n \). If the value of \( n // k \) is odd, the output is 'YES'. If the value of \( n // k \) is even, the output is 'NO'.
#Overall this is what the function does:The function accepts two positive integers `n` and `k`, which must satisfy the conditions \( 1 \leq n, k \leq 10^{18} \) and \( k \leq n \). It calculates the integer division of `n` by `k`, checks if the result is odd or even, and prints 'YES' if it is odd, and 'NO' if it is even. There are no return values from the function; instead, it directly outputs the result.

