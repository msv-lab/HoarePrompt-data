#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones with length n.
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
        
    #State of the program after the  for loop has been executed: `comps` is a list where each element contains a positive integer representing the connected component of each index in the permutation, `col` is equal to the number of distinct connected components in the permutation, `n` is an integer such that 1 ≤ `n` ≤ 200,000, and `p` is a list of integers representing a valid permutation of numbers from 1 to `n`.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts an integer `n`, a list `p` that is a permutation of integers from 1 to `n`, and a list `b` consisting of zeros and ones. It calculates the number of distinct connected components in the permutation `p`, returning 0 if there is only one connected component, or the count of components otherwise. Additionally, if the sum of the elements in `b` is zero, it returns an additional 1 to the final result. Therefore, it effectively returns the number of connected components in the permutation minus 1 if there is at least one element in `b` that is 1.

