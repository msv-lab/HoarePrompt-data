#State of the program right berfore the function call: **
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
        
    #State of the program after the  for loop has been executed: `n` is greater than 1, `p` is a list of integers where each element is `n - 1`, `b` contains the input values converted to integers, `comps` is a list where all elements are equal to `n`, `col` is `n`, `i` is `n-1`, and `j` is updated to the final value based on the chain of indices in list `p`, and `comps` is updated accordingly with `col`. The loop has finished executing, and all elements in `comps` have been updated to `col` where the loop condition was satisfied.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` takes user input, processes it, and prints a value based on certain conditions. It does not accept any parameters and does not return any value. The code initializes variables, processes the input data to update the `comps` list, calculates the value of `col`, and prints the sum of 0 or 1 based on the conditions.

