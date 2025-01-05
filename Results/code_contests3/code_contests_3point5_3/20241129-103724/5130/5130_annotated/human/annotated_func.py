#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 <= n <= 2*10^5.
- p is a sequence of integers where each element pi is an integer such that 1 <= pi <= n.
- b is a sequence of integers consisting of zeros and ones.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `p` is a list containing `n` elements, `b` is a map object created by applying the `int` function to each element obtained by splitting the input using `raw_input().split()`, `comps` is a list of `n` elements all assigned the value of `col` + 1, `col` is incremented by 1, `j` is updated to the value of `p[j]` after the loop finishes.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads inputs for `n`, `p`, and `b` according to the given constraints. It then iterates through the elements of `p` and assigns components based on certain conditions. After the loop, it prints a value based on the calculated `col` and the sum of elements in `b`. The function does not return any value but operates on the predefined inputs.

