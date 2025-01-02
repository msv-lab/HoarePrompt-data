#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 10^5.
def func():
    n, m = map(int, stdin.readline().split())
    edges, cur = [], 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if not m:
                break
            if gcd(i, j) == 1:
                m -= 1
                edges.append('%d %d' % (i, j))
                cur = max(cur, j)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `m` is the original `m` minus the number of pairs `(i, j)` where `gcd(i, j) == 1` (and will be 0 if there were enough valid pairs), `edges` is a list of strings representing pairs `(i, j)` where `gcd(i, j) == 1`, `cur` is the maximum value of `j` for which `gcd(i, j) == 1` was true during the loop execution, or 0 if no such pairs exist.
    if (m or cur != n) :
        print('Impossible')
    else :
        print('%s\n%s' % ('Possible', '\n'.join(edges)))
    #State of the program after the if-else block has been executed: *`n` is an integer such that \(1 \leq n \leq 10^5\), `m` is the original `m` minus the number of pairs `(i, j)` where `gcd(i, j) == 1` (and will be 0 if there were enough valid pairs), `edges` is a list of strings representing pairs `(i, j)` where `gcd(i, j) == 1`, `cur` is the maximum value of `j` for which `gcd(i, j) == 1` was true during the loop execution, or 0 if no such pairs exist. If either `m` is non-zero or `cur` is not equal to `n`, the string 'Impossible' has been printed. Otherwise, `m` is 0 and `cur` is equal to `n`.
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from standard input, where `1 ≤ n, m ≤ 10^5`. It then attempts to find `m` pairs of integers `(i, j)` such that `1 ≤ i < j ≤ n` and the greatest common divisor (GCD) of `i` and `j` is 1. These pairs are stored in a list `edges`. After attempting to find these pairs, the function checks if it successfully found exactly `m` pairs and if the largest `j` used in these pairs is equal to `n`. If both conditions are met, it prints "Possible" followed by the pairs. If either condition fails, it prints "Impossible". The function does not return any value; it only prints the result.

