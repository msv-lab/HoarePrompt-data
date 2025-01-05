#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000); p is a list of integers representing a valid permutation of integers from 1 to n; b is a list of integers consisting of zeros and ones with a length of n.
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
        
    #State of the program after the  for loop has been executed: `comps` is a list where each element corresponds to the connected component index based on the relationships defined in `p`, `col` is the total number of distinct connected components identified, `n` is the input integer, and `p` is a list derived from the input integers.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts an integer `n`, a list `p` representing a valid permutation of integers from 1 to `n`, and a list `b` consisting of zeros and ones. It calculates the number of distinct connected components in the permutation defined by `p` and checks if the sum of the list `b` is zero. The function returns 0 if there is only one connected component, the total number of connected components otherwise, and adds 1 if the sum of `b` is zero.

