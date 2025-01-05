#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2·10^5), p is a list of integers representing a permutation of numbers from 1 to n, and b is a list of integers consisting of zeros and ones with a length of n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `comps` contains component numbers for each index from `0` to `n-1`, `col` is the number of unique components identified in the permutation.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` that represents a permutation of integers from 1 to `n`, and a list `b` of zeros and ones. It calculates the number of unique components in the permutation and checks if the sum of the list `b` is zero. The function returns 0 if there is only one component, otherwise it returns the number of components. Additionally, if the sum of `b` is zero, it adds 1 to the result. Thus, the output can be 0, the number of components, or the number of components plus 1 if the sum of `b` is zero.

