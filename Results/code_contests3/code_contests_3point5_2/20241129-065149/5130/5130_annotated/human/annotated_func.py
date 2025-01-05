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
        
    #State of the program after the  for loop has been executed: `Error: raw_input() is not defined`, `n` is defined with an integer value, all elements in `comps` are assigned a unique value of `col`, `col` is incremented by 1 for each unique element, `i` is equal to `n-1`, `j` is assigned the value of the last element in the sequence `p`, all elements in `comps` have been updated according to the loop conditions
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values, processes them to assign unique values to elements in `comps`, and then prints a value based on the conditions. It does not accept any parameters. The returned value is based on the calculated conditions inside the function. The function increments `col` for each unique element in `comps` and updates elements according to loop conditions. If `col` is 1, it prints 0, otherwise it prints `col`. Additionally, if the sum of elements in `b` is 0, it adds 1 to the printed value.

