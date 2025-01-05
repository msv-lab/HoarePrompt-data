#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), x is a positive integer (1 ≤ x ≤ 10^9), and a is a list of n positive integers (1 ≤ a_i ≤ 10^9).
def func_1(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a, x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i] / x)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `mx` is the sum of math.ceil(a[i] / x) for all i in range(n), `somme` is the sum of elements in a, `a` is a list of n positive integers.
    print('{} {}'.format(int(somme / x), int(mx)))
#Overall this is what the function does:The function accepts three parameters: a positive integer `n`, a positive integer `x`, and a list `a` of `n` positive integers. It calculates the total sum of the elements in `a` and also computes the ceiling of the division of each element in `a` by `x`. Finally, it prints two values: the integer part of the total sum divided by `x` and the sum of the ceiling values. The function does not return any value; it only prints the results.

