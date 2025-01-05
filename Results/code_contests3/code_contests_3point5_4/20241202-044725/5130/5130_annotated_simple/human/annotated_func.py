#State of the program right berfore the function call: **
def func():
    n = int(raw_input())
    p = [(int(v) - 1) for v in raw_input().split()]
    b = map(int, raw_input().split())
    comps = [(0) for i in xrange(n)]
    col = 0
    for i in xrange(n):
        if comps[i] == 0:
            col += 1
            comps[i] = col
            j = i
            while comps[p[j]] == 0:
                j = p[j]
                comps[j] = col
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `i` is equal to `n-1`, `b` is a mapped list of integers, `comps` is a list where each element is equal to the final value of `col`, `col` is equal to the total number of times the loop executed, `j` is updated to the last accessed element from list `p` before encountering a non-zero value in `comps`, `comps[p[j]]` is not equal to 0.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input from the user, processes the data, and prints a result based on the calculations. It does not accept any parameters and does not return any values. The function calculates certain values based on the input provided by the user and prints the result.

