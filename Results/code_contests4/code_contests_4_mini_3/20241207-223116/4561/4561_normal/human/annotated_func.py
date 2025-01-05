#State of the program right berfore the function call: n is a positive integer representing the number of colliders, and m is a positive integer representing the number of requests, where each request is in the form of "+ i" or "- i" and 1 <= i <= n.
def func_1(n):
    prim[1] = 1
    for i in range(2, n):
        if not prim[i]:
            for j in range(i, n, i):
                prim[j] = i
        
    #State of the program after the  for loop has been executed: `n` is a positive integer greater than 2, `m` is a positive integer, `prim[i]` is the smallest prime number that divides `i` for all `i` from 2 to `n-1`, and `prim[1]` is 1.
#Overall this is what the function does:The function accepts a positive integer `n`, initializes a list of smallest prime factors for integers from 2 to `n-1`, but does not process any requests or update the state of colliders as described in the annotations.

#State of the program right berfore the function call: x is a tuple where the first element is a positive integer n (the number of colliders) and the second element is a positive integer m (the number of requests), followed by m strings representing the requests in the form of either "+ i" or "- i" (1 ≤ i ≤ n).
def func_2(x):
    fac = []
    while x > 1:
        div = prim[x]
        
        fac.append(div)
        
        while x % div == 0:
            x //= div
        
    #State of the program after the loop has been executed: `x` is a tuple where the first element is reduced to a value that is not divisible by any remaining elements in `prim`, `fac` contains all the prime factors of the original first element of `x` in the order they were found, and `x` has been fully factored.
    return fac
    #The program returns the list of prime factors 'fac' of the original first element of the tuple 'x', in the order they were found.
#Overall this is what the function does:The function accepts a tuple `x` where the first element is a positive integer and returns a list of its prime factors in the order they were discovered. The function does not process the second part of the tuple which includes requests, hence it only focuses on factoring the first integer. If the input integer is 1 or less, it will return an empty list since there are no prime factors for such values.

