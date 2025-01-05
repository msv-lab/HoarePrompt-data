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
        
    #State of the program after the  for loop has been executed: Output State: `n` is greater than 0, `col` is equal to the number of unique elements in `p`, `comps` is a list of `n` elements where each element represents a unique component identified in the loop, all components have been assigned a unique identifier.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values, processes them to identify unique components, and prints a value based on certain conditions. It does not accept any parameters and does not have a specific return value. The functionality of the function is to determine the number of unique components and output either 0 or the count of unique components based on the sum of the values in list `b`.

