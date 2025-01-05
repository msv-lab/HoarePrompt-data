#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones, with the same length as p.
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
        
    #State of the program after the  for loop has been executed: `comps` is a list where each element indicates the component index of the corresponding index in the permutation `p`, `col` is the total number of components formed, `n` is a positive integer such that 1 ≤ `n` ≤ 200,000.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` representing a permutation of numbers from 1 to `n`, and a list `b` consisting of zeros and ones. It calculates and counts the number of connected components in the permutation `p`. The function returns 0 if there is only one component; otherwise, it returns the count of components. Additionally, if the sum of the elements in `b` is zero, it adds 1 to the result.

