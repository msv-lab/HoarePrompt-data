#State of the program right berfore the function call: K is an integer such that 2 ≤ K ≤ 2500, and S is an integer such that 0 ≤ S ≤ 3K.
def func():
    k, s = map(int, raw_input().split())
    patterns = []
    ct = 0
    for x in range(k + 1):
        nokori = s - x
        
        for y in range(k + 1):
            if 0 <= nokori - y <= k:
                ct += 1
        
    #State of the program after the  for loop has been executed: `k` is an integer within the range \(2 \leq k \leq 2500\), `s` is an integer within the range \(0 \leq s \leq 3k\), `patterns` is an empty list, `ct` is the total count of valid `(x, y)` pairs that satisfy \(0 \leq s - x - y \leq k\) over all iterations of the loop, `x` is `k + 1`, and `nokori` is `s - ct \cdot (k + 1)`
    print(ct)
#Overall this is what the function does:The function accepts no explicit parameters but reads two integers `K` and `S` from standard input, where \(2 \leq K \leq 2500\) and \(0 \leq S \leq 3K\). It then iterates through all possible pairs \((x, y)\) where \(0 \leq x \leq K\) and \(0 \leq y \leq K\), counting the number of valid pairs \((x, y)\) that satisfy the condition \(0 \leq S - x - y \leq k\). After completing the iteration, it prints the count of valid pairs. If `K` is out of range, the function does not handle this case explicitly and may raise an error when converting input. Similarly, if `S` is out of range, the function also does not handle this case explicitly and may raise an error when converting input. The final state of the program is that the variable `ct` contains the count of valid pairs, which is printed to the console.

