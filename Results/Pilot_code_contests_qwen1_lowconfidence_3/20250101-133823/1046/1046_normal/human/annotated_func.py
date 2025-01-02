#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^3, and P is a list of n integers where each integer p_i satisfies 0 ≤ p_i < i.
def func_1(line):
    """Read example from stdin and parse it into the appropriate data structure

    Use in the following way:

    example = example_generator(stdin_generator)
    while True:
        numbers, target = next(example)
        .
        .
        .

    """
    while True:
        n = int(next(line).strip())
        
        P = [(int(p_i) - 1) for p_i in next(line).split()]
        
        yield n, P
        
    #State of the program after the loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^3\); `P` is a list of `n` integers where each integer \(p_i\) in `P` is one less than the corresponding integer read from the input.
#Overall this is what the function does:The function `func_1` reads pairs of values from standard input (represented by the `line` parameter), where each pair consists of an integer `n` and a list `P` of `n` integers. The integer `n` represents the number of elements in the list `P`. Each element `p_i` in the list `P` is an integer that is one less than the corresponding integer read from the input. The function yields these pairs indefinitely until the end of the input stream. The state of the program after each iteration of the loop is that `n` is an integer within the range \(1 \leq n \leq 10^3\), and `P` is a list of `n` integers where each integer \(p_i\) in `P` is one less than the corresponding integer read from the input. If the input stream ends, the function will stop yielding pairs.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10³, and p is a list of n integers where 1 ≤ p[i] ≤ i for each 0 ≤ i < n.
def func_2(n, p):
    """Print out the number of times Vasya needs to use portals to get to room n+1

    dp[i] is the number of portal jumps required to start off at room i with an odd
    number of crosses and get back to room i with an even number of crosses.

    Hence the recurrence relation is as follows:

    dp[i] = 1 + [Sum_{j = p(i)}^{i-1} dp[j] + 1]

    This can be read as "the number of portal jumps to get from room i with an odd
    number of crosses to an even number of crosses is equivalent to taking a portal
    jump to room p(i) into an odd number of crosees (+1), getting back into that
    state with an even number of crosses (Sum part).

    """
    dp = [0] * n
    for i in range(n):
        portal_jumps = 1
        
        for j in range(p[i], i):
            portal_jumps += dp[j] % (1000000000.0 + 7)
            portal_jumps += 1 % (1000000000.0 + 7)
        
        dp[i] = int(portal_jumps % (1000000000.0 + 7))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^3\), `p` is a list of `n` integers where \(1 \leq p[i] \leq i\) for each \(0 \leq i < n\), `dp` is a list of `n` elements, each element is \((n + 1) \% 1000000007\).
    total_pjumps = 0
    for i in range(n):
        total_pjumps += dp[i] % (1000000000.0 + 7)
        
        total_pjumps += 1 % (1000000000.0 + 7)
        
    #State of the program after the  for loop has been executed: `total_pjumps` is equal to \(\left( (n + 1) \mod 1000000007 + \sum_{i=0}^{n-1} dp[i] + n \right) \mod 1000000007\), `i` is \(n\), `n` is an integer such that \(1 \leq n \leq 10^3\).
    print(total_pjumps)
#Overall this is what the function does:The function `func_2` accepts two parameters: an integer `n` and a list `p` of length `n`. It calculates the number of portal jumps required for Vasya to get from each room `i` (with an odd number of crosses) to another room with an even number of crosses and back, using the given portal connections defined by `p`. After performing these calculations, it sums up the total number of portal jumps required for all rooms and prints this sum modulo \(1000000007\). The function does not return a value; instead, it directly prints the result. Potential edge cases include invalid input values for `n` or `p`, which the function currently does not handle. If `n` is outside the range \(1 \leq n \leq 10^3\) or any element in `p` does not satisfy \(1 \leq p[i] \leq i\), the function will produce unexpected results due to the lack of validation.

