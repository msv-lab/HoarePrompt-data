#State of the program right berfore the function call: **Precondition**: **n is an integer such that 1 ≤ n ≤ 2·10^5. p is a list of n integers where each integer is between 1 and n. b is a list of n integers where each integer is either 0 or 1.**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 2·10^5, `p` is a list of n integers where each integer is between 0 and n-1, `b` is a map object of n integers, `comps` is a list of n integers where each element is updated to a unique value, `col` is the total number of unique values assigned to `comps` during the loop execution.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values `n`, `p`, and `b` from the user. It then processes the values to assign unique components represented by `comps`. After that, it prints either 0 or the total number of unique components based on certain conditions. The function does not explicitly return a value.

