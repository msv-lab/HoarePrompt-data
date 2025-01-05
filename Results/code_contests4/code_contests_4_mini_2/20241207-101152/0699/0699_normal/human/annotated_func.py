#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), x is a positive integer (1 ≤ x ≤ 10^9), and a is a list of n positive integers (1 ≤ a_i ≤ 10^9).
def func_1(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a, x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i] / x)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is equal to `n`, `mx` is equal to the sum of math.ceil(a[i] / x) for all i in range(n), `somme` is the sum of the elements in the list `a`, `a` is a list of n positive integers.
    print('{} {}'.format(int(somme / x), int(mx)))
#Overall this is what the function does:The function accepts a positive integer `n`, a positive integer `x`, and a list of `n` positive integers `a`. It calculates the total sum of the elements in `a` and divides each element by `x` using ceiling division to get a count of how many times `x` fits into each element. The function then prints two values: the integer division of the total sum by `x`, and the total count of ceiling divisions. The function does not return any value; it only prints the results.

