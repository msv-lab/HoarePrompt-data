#State of the program right berfore the function call: n is a positive integer. The sequences p and b are lists of integers with length n, where each element in p is between 1 and n, and each element in b is either 0 or 1.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `p` is a list of integers with length n where each element is between 0 and n-1, `b` is a list of integers with length n where each element is either 0 or 1, `comps` is a list of n elements where each element is assigned the value of the number of unique connected components in the graph represented by the lists `p` and `b`, `col` is the total number of unique connected components in the graph
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values for `n`, `p`, and `b` according to specified constraints. It then calculates the number of unique connected components in a graph represented by `p` and `b` and prints the result. The function does not explicitly return any value.

