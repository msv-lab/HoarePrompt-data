#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 ≤ n ≤ 2*10^5.
- p is a sequence of integers where each element pi is an integer such that 1 ≤ pi ≤ n.
- b is a sequence of integers consisting of zeros and ones, where each element bi is either 0 or 1.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `p` is a list of integers with each value decreased by 1, `comps` is a list of `n` elements where each element is a unique value between 1 and `n`, `col` is equal to the number of unique elements in `comps`, `i` is `n-1`, `j` is the last valid index where `comps[p[j]]` is not equal to 0.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function func reads input values for n, p, and b. It then computes the number of connected components in a graph based on the input sequences p and b. The function prints either 0 or the number of connected components depending on certain conditions. The function does not return any value.

