#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers consisting of zeros and ones, with length equal to n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `comps` is a list where each index has been assigned a unique value from 1 to `col` based on the connectivity defined by `p`, `col` is the total number of unique components identified, `b` remains unchanged, `p` is a list of integers from 0 to n-1, and `i` is equal to `n-1` after the loop finishes executing.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 200,000), a list `p` that is a permutation of numbers from 1 to `n`, and a list `b` consisting of zeros and ones of length `n`. It identifies the number of unique connected components in the permutation defined by `p` and checks the sum of the list `b`. The function returns 0 if there is only one connected component, and adds 1 if the sum of `b` is 0. Thus, the function effectively returns the number of unique components minus one if there is at least one component and increments the result by 1 if there are no 1's in `b`.

