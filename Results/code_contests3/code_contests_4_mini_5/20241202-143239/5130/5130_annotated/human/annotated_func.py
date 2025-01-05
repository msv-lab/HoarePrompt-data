#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000), p is a list of integers representing a valid permutation of integers from 1 to n, and b is a list of integers consisting of zeros and ones with a length of n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 200,000), `comps` contains integers from 1 to `col` where each integer represents the component index for the corresponding nodes, `col` is the total number of distinct components identified, and `p` remains unchanged as a list of integers from 0 to n-1.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` representing a valid permutation of integers from 1 to `n`, and a list `b` consisting of zeros and ones. It identifies the number of distinct components in the permutation and checks if the sum of list `b` is zero. The function then outputs `0` if there is only one component, or the number of components if there are multiple, and adds `1` if the sum of `b` is zero.

