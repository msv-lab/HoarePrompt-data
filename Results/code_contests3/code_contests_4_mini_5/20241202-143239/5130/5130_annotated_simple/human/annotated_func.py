#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones, with a length equal to n.
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
        
    #State of the program after the  for loop has been executed: `comps` contains integers representing the component labels of the permutation from `p`, `col` is the total number of distinct components identified in the permutation, `n` is a positive integer such that 1 ≤ `n` ≤ 200,000.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a permutation list `p` of integers from 1 to `n`, and a binary list `b` of length `n`. It computes the number of distinct components in the permutation represented by `p`. If there is only one component, it returns 0; otherwise, it returns the number of components. Additionally, if the sum of the elements in `b` is 0, it adds 1 to the result, effectively returning `col` if there are multiple components, or 1 if there are no components and `b` consists entirely of zeros.

