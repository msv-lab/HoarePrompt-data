#State of the program right berfore the function call: **
def func_1(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a, x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i] / x)
        
    #State of the program after the  for loop has been executed: `x` is a floating-point number, `mx` is the sum of math.ceil(a[i] / x) for each i in the range of n, `a` is a list of values, `n` is the length of the list `a`
    print('{} {}'.format(int(somme / x), int(mx)))
#Overall this is what the function does:The function `func_1` accepts three parameters `n`, `x`, and `a`. It converts `x` to a floating-point number, calculates the sum of values in list `a`, and then iterates over the range of `n` to calculate the sum of `math.ceil(a[i] / x)` for each element in `a`. Finally, it prints the integer division of the sum of values in `a` by `x` and the total sum of `math.ceil(a[i] / x)` values. The function does not have a specified return value.

