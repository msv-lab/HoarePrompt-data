#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a sequence of integers representing a permutation of numbers from 1 to n; b is a sequence of integers consisting of zeros and ones with a length of n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `p` is a list of integers decreased by 1 from the input values, `b` is a list of integers from the input values, `comps` is a list where each element represents the component number assigned based on the connections defined in `p`, `col` is the total number of unique components identified, and `i` is equal to `n` after the loop.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function reads a positive integer `n`, a permutation `p` of integers from 1 to `n`, and a binary sequence `b` of length `n`. It identifies the number of unique connected components in the permutation and returns the number of components minus one if there is more than one component, or 0 if there is only one component. Additionally, if the sum of the binary sequence `b` is zero, it adds 1 to the result. Therefore, the function effectively returns a value based on the connected components formed by the permutation and whether the binary sequence consists solely of zeros.

