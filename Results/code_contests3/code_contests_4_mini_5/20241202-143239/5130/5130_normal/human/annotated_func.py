#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of numbers from 1 to n; and b is a list of integers consisting of zeros and ones, with a length equal to n.
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
        
    #State of the program after the  for loop has been executed: `comps` is a list where each index contains the component identifier (1 to the final value of `col`) for the corresponding permutation group, `col` is the total number of distinct components in the permutation, and `n` is the input integer representing the size of the permutation.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` which is a permutation of numbers from 1 to `n`, and a list `b` consisting of zeros and ones with length `n`. It calculates the number of distinct components in the permutation and checks if there are no ones in list `b`. If there is only one component, it returns 0; otherwise, it returns the number of distinct components, adding 1 if `b` contains only zeros.

