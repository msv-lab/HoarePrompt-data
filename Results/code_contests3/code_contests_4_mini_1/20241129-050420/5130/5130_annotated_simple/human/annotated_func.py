#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of length n where each integer is in the range [1, n]; and b is a list of integers consisting of zeros and ones with length n.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200,000; `comps` contains the component identifiers for each index based on the mapping defined by `p`; `col` is the total number of distinct components identified; `p` is a list of integers representing the mapping of indices.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts an integer `n`, a list `p` representing a permutation of integers from 1 to `n`, and a list `b` consisting of zeros and ones. It identifies the number of distinct components in the permutation `p` and checks if all values in list `b` are zeros. The function returns the number of distinct components minus one if there is more than one component, or zero if there is only one component, and adds one to the result if all values in `b` are zeros.

