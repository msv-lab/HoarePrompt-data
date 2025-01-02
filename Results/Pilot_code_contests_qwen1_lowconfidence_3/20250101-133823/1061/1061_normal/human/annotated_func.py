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
        
    #State of the program after the  for loop has been executed: `k` is an integer such that \(2 \leq k \leq 2500\), `s` is an integer such that \(0 \leq s \leq 3k\), `patterns` is an empty list, `ct` is the count of all valid pairs \((x, y)\) where both \(x\) and \(y\) are in the range \([0, k]\) and satisfy \(0 \leq s - x - y \leq k\).
    print(ct)
#Overall this is what the function does:The function `func` accepts two parameters: `K` and `S`. `K` is an integer such that \(2 \leq K \leq 2500\), and `S` is an integer such that \(0 \leq S \leq 3K\). After executing the function, it counts the number of valid pairs \((x, y)\) where both \(x\) and \(y\) are in the range \([0, k]\) and satisfy \(0 \leq s - x - y \leq k\). If the input values of `K` and `S` are within their specified ranges, the function prints the count of these valid pairs. Otherwise, the function does not return any specific value and the behavior is undefined since no error handling is implemented.

