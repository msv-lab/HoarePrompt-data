#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 1 000 000.
def func():
    n, m = map(int, input().split())

count = 0
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x + y) % 5 == 0:
                count += 1
        
    #State of the program after the  for loop has been executed: x is n + 1, count is the total number of pairs (x, y) such that (x + y) % 5 == 0 for all x in the range from 1 to n and all y in the range from 1 to m, and m remains the same.
    print(count)
#Overall this is what the function does:The function reads two positive integers `n` and `m` from standard input, where \(1 \leq n, m \leq 1,000,000\). It then iterates through all possible pairs \((x, y)\) where \(x\) ranges from 1 to \(n\) and \(y\) ranges from 1 to \(m\), counting the number of pairs where the sum \(x + y\) is divisible by 5. After completing the iteration, it prints the total count of such pairs. The function does not accept any parameters and returns nothing, but its output is the count of valid pairs.

