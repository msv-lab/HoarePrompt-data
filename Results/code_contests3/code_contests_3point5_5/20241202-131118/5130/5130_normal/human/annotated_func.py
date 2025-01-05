#State of the program right berfore the function call: **Precondition**: 
- n is a positive integer such that 1 ≤ n ≤ 2·10^5.
- p is a sequence of integers of length n such that each element pi is in the range 1 ≤ pi ≤ n.
- b is a sequence of zeros and ones of length n.
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
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `p` is a list of integers where each element is 1 less than the input values, `i` is equal to n-1, `comps` is a list of n elements where each element is incremented by 1, `col` is equal to the total number of unique components in comps, `j` is such that `p[j]` is a valid index in `comps` and `comps[p[j]]` is not equal to 0, `j` is updated based on the value at index `j` in list `p`, `comps[j]` is assigned the value of `col`, the loop stops when there are no more valid indices left in p.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input for `n`, `p`, and `b` according to given constraints. It then calculates the number of unique components in `p` and returns either 0 or the count of unique components incremented by 1 based on certain conditions.

