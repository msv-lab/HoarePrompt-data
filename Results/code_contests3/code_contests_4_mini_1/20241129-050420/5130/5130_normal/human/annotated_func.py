#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200,000); p is a list of integers representing a permutation of integers from 1 to n; b is a list of integers consisting of zeros and ones, with a length equal to n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `comps` contains the component labels assigned to each index based on the visited indices in the permutation `p`, `col` is the total number of unique components identified, and `j` is the last index accessed in the permutation during the loop execution.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n`, a list `p` representing a permutation of integers from 1 to `n`, and a list `b` of zeros and ones. It identifies the number of unique components in the permutation and checks if all elements in `b` are zeros. The function returns the number of unique components minus one if there is more than one component, or zero if there is only one component, and adds one if all elements in `b` are zeros.

