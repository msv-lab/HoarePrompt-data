#State of the program right berfore the function call: n and m are even and positive integers such that 2 ≤ n, m ≤ 10^9, and k is an integer such that 0 ≤ k < n·m.
def func():
    n, m, k = map(int, input().split())
    k %= n * 2 - 2
    if (k < n - 1) :
        print(k + 1, 1)
    else :
        if (k < n * 2 - 2) :
            print(n - (k - n + 1) % (n - 1) - 1, (k - n + 1) // (n - 1) + 1)
        else :
            print(1, 2)
        #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. If \( k < n * 2 - 2 \), the output is \( 2n - k - 2 \) and `1`. If \( k \geq n * 2 - 2 \), the values of `n`, `m`, and `k` remain as per the precondition.
    #State of the program after the if-else block has been executed: *`n`, `m`, and `k` are integers. If \( k < n - 1 \), then the output is \( 2n - k - 2 \) and `1`. Otherwise, the values of `n`, `m`, and `k` remain as per the precondition.
#Overall this is what the function does:The function processes three input integers \( n \), \( m \), and \( k \), where \( n \) and \( m \) are even and positive integers within the range \( 2 \leq n, m \leq 10^9 \) and \( k \) is an integer within the range \( 0 \leq k < n \cdot m \). It calculates and prints coordinates based on the value of \( k \).

Specifically, the function first reduces \( k \) modulo \( n \cdot 2 - 2 \). Then, depending on the value of \( k \):

- If \( k < n - 1 \), it prints \( (k + 1, 1) \).
- If \( k \geq n - 1 \) and \( k < n \cdot 2 - 2 \), it calculates the row and column indices as follows:
  - Row index: \( 2n - k - 2 \)
  - Column index: \( \left(\frac{k - n + 1}{n - 1}\right) + 1 \)
  - It prints the calculated row and column indices.
- If \( k \geq n \cdot 2 - 2 \), it prints \( (1, 2) \).

This process ensures that the function handles all possible values of \( k \) and provides appropriate output coordinates based on the given conditions.

