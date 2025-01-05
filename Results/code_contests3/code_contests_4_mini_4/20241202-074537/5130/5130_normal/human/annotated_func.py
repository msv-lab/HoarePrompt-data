#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a list of n integers representing a valid permutation of numbers from 1 to n; and b is a list of n binary integers (0s and 1s).
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000; `comps` is a list of integers where each element indicates the component number for the corresponding index; `col` is the total count of distinct connected components found in `p`.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function reads an integer `n` and two lists: `p`, which is a permutation of integers from 1 to `n`, and `b`, which contains binary integers (0s and 1s). It determines the number of distinct connected components in the permutation `p`, returning 0 if there is only one component, or the total number of components plus 1 if the sum of elements in `b` is 0. The function does not explicitly accept parameters but processes inputs from standard input. It assumes valid input as per the stated constraints.

