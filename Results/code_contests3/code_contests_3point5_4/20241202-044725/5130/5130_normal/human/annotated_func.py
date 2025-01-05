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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `p` is a list containing n elements, `b` is a list containing n elements, `comps` is a list of n elements where each element is a unique value between 1 and the number of connected components in the graph represented by `p`, `col` is equal to the number of connected components in the graph represented by `p`
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input and processes it to determine the number of connected components in a graph represented by the input. It then prints either 0 if there is only one connected component or the number of connected components in the graph. Additionally, it increments the output by 1 if the sum of elements in list `b` is 0. The function does not accept any parameters and returns the output based on the processed input data.

