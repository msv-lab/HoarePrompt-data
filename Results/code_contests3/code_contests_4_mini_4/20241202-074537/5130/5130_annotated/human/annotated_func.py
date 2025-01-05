#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), p is a list of integers representing a valid permutation of length n where each integer is between 1 and n, and b is a list of integers of length n consisting of zeros and ones.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200,000), `comps` is a list where each index contains the component identifier (a positive integer) for each element in the mapped iterable `p`, `col` is the total number of distinct components identified in the list `p`.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a valid permutation list `p` of integers from 1 to `n`, and a binary list `b` of length `n`. It identifies the number of distinct components in the permutation and returns 0 if there is only one component, or the number of distinct components if there are multiple. Additionally, if the sum of the binary list `b` is 0, it adds 1 to the result. Therefore, the function returns the number of distinct components minus one if there are multiple components and the sum of `b` is zero.

