#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 200,000; p is a list of integers representing a permutation of numbers from 1 to n; b is a list of integers containing only 0s and 1s, with a length equal to n.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 200,000, `comps` contains component numbers for each index from 1 to `col`, and `col` is the total number of distinct components in the permutation defined by `p`.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function accepts a positive integer `n` and two lists: `p`, which is a permutation of integers from 1 to `n`, and `b`, which contains only 0s and 1s with a length equal to `n`. It calculates the number of distinct components in the permutation defined by `p`. The function returns 0 if there is only one component; otherwise, it returns the total number of distinct components plus 1 if the sum of `b` is 0, indicating that all entries in `b` are 0.

