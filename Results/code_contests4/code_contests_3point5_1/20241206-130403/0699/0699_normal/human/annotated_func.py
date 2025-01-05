#State of the program right berfore the function call: **
def func_1(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a, x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i] / x)
        
    #State of the program after the  for loop has been executed: `x` is converted to a float, `mx` is increased by the sum of the ceiling values of all elements in `a` divided by `x`, `i` is `n-1`, `n` is the total number of elements in `a`
    print('{} {}'.format(int(somme / x), int(mx)))
#Overall this is what the function does:The function `func_1` accepts three parameters: `n`, `x`, and `a`. It converts `x` to a float, calculates the sum of elements in `a`, and then iterates over `n` elements in `a` to increment `mx` by the ceiling value of each element divided by `x`. Finally, it prints the integer division of the sum of `a` by `x` and the calculated `mx`. The function does not have a return value and simply prints the results.

