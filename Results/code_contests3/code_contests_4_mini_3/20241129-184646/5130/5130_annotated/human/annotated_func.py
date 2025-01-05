#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000); p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones, with the same length as p.
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
        
    #State of the program after the  for loop has been executed: `n` is an input positive integer (1 ≤ n ≤ 200,000), `comps` contains values from 1 to `col` indicating the connected components in the permutation represented by `p`, `col` is the total number of connected components found in `p`, and `b` remains a list of zeros and ones, unchanged.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` which is a permutation of numbers from 1 to `n`, and a list `b` consisting of zeros and ones. It calculates the number of connected components in the permutation represented by `p` and checks if the list `b` contains only zeros. It then prints `0` if there is only one connected component and `1` if the sum of `b` is zero, otherwise it prints the number of connected components.

