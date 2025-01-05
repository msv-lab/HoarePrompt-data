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
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `p` is a list of integers where each element is input integer - 1, `b` is a list of integers obtained from the input split by spaces, `comps` is updated such that all elements have been assigned a value corresponding to the component they belong to, `col` is the total number of components, `i` is equal to `n-1`, `j` is a value that eventually leads to a cycle based on the values of `p`
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values, calculates the components based on the input data, and prints either 0 or the total number of components based on conditions. It does not accept any parameters and does not return any value.

