#State of the program right berfore the function call: n and m are non-negative integers such that 0 ≤ n, m ≤ 1 000 000 and n + m > 0.
def func():
    n, m = map(int, input().split())

towers = set()
    for i in range(1, n + 1):
        towers.add(i * 2)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(0 < n \leq 1,000,000\), `m` is a non-negative integer such that \(0 \leq m \leq 1,000,000\) and \(n + m > 0\), `towers` is a set containing {2, 4, 6, ..., 2n}, `i` is `n`.
    for i in range(1, m + 1):
        towers.add(i * 3)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(0 < n \leq 1,000,000\), `m` is a non-negative integer such that \(0 \leq m \leq 1,000,000\) and \(n + m > 0\), `towers` is a set containing {2, 4, 6, ..., 2n, 3, 6, 9, ..., 3m}, `i` is `n`. The loop executes if `m` is greater than 0. If `m` is 0, the loop does not execute, and `towers` remains {2, 4, 6, ..., 2n}.
    print(max(towers))
#Overall this is what the function does:The function `func` reads two non-negative integers `n` and `m` from the input, where \(0 \leq n, m \leq 1,000,000\) and \(n + m > 0\). It then constructs a set `towers` that contains even numbers up to \(2n\) and multiples of 3 up to \(3m\). Finally, the function prints the maximum value in the `towers` set. If either `n` or `m` is zero, the corresponding loop will not add any elements to the set, but the function will still print the maximum value from the non-empty part of the set. If both `n` and `m` are zero, the function will not execute due to the condition \(n + m > 0\).

