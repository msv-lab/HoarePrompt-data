#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100,000), x is a positive integer (1 ≤ x ≤ 1,000,000,000), and a is a list of integers where each element a_i satisfies (1 ≤ a_i ≤ 1,000,000,000). The sum of n across all test cases does not exceed 100,000.
def func_1(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a, x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i] / x)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100,000), `mx` is the sum of math.ceil(a[i] / x) for all i from 0 to n-1, `a` is a list of integers, `x` is a positive float.
    print('{} {}'.format(int(somme / x), int(mx)))
#Overall this is what the function does:The function accepts a positive integer `n`, a positive integer `x`, and a list of integers `a`. It calculates the total sum of the elements in `a` and the sum of the ceiling of each element in `a` divided by `x`. It then prints two values: the integer division of the total sum by `x` and the sum of the ceilings. The function does not explicitly return any value.

