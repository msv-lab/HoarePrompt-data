#State of the program right berfore the function call: n is an integer such that 1 <= n <= 2*10^5. p is a list of integers representing a permutation where each element is between 1 and n. b is a list of integers consisting of zeros and ones.**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 2*10^5, `p` is a list of integers, `b` is a list of integers, `comps` is a list of integers where each element corresponds to a unique color group, `col` is equal to the total number of unique color groups created in `comps`.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values for `n`, `p`, and `b`, then processes these inputs to create color groups based on the permutation `p`. It prints either 0 or the total number of unique color groups depending on specific conditions. The function does not explicitly return a value.

