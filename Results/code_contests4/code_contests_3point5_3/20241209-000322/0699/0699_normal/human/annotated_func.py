#State of the program right berfore the function call: **
def func_1(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a, x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i] / x)
        
    #State of the program after the  for loop has been executed: `x` is a float, `mx` is the sum of ceiling values of all elements in a divided by x, `i` is the value of n-1, `n` is the total number of elements in a, for the loop to execute `n` must be greater than 0
    print('{} {}'.format(int(somme / x), int(mx)))
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `x`, and `a`. The function converts `x` to a float, calculates the sum of all elements in `a`, and then iterates through a loop to calculate the sum of ceiling values of elements in `a` divided by `x`. The function prints the integer division result of the sum of `a` divided by `x` and the total sum of ceiling values. The function does not have a specific return value. Potential edge cases include ensuring `n` is greater than 0 for the loop to execute correctly.

