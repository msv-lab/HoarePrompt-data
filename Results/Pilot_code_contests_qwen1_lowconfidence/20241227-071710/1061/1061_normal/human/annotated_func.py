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
        
    #State of the program after the  for loop has been executed: `ct` is the total count of valid `(x, y)` pairs where both `x` and `y` are in the range `[0, k]` and satisfy the condition `0 <= s - x - y <= k`, `nokori` is the remaining value of `s - x` after the outer loop, `y` is the last value of `y` considered in the inner loop, and `x` is the last value of `x` considered in the outer loop.
    print(ct)
#Overall this is what the function does:The function `func` accepts two parameters: `K` and `S`, where `K` is an integer in the range [2, 2500] and `S` is an integer in the range [0, 3K]. The function iterates through all possible values of `x` and `y` in the range [0, K] and counts the number of valid `(x, y)` pairs that satisfy the condition `0 <= s - x - y <= k`. After executing the loops, the function prints the count of valid pairs. There are no return statements in the provided code, so the function does not return anything.

