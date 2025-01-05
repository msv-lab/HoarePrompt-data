#State of the program right berfore the function call: k is an integer between 2 and 1000, a is a positive integer representing the number of nuts, b is a positive integer representing the number of divisors, and v is a positive integer representing the capacity of each section of the box, all within the range of 1 to 1000.
def func():
    k, a, b, v = [int(x) for x in raw_input().split()]
    res = 0
    while a > 0:
        res += 1
        
        if b >= k:
            a = a - k * v
            b = b - (k - 1)
        elif b > 0:
            a = a - (b + 1) * v
            b = 0
        else:
            a = a - v
        
    #State of the program after the loop has been executed: `a` is less than or equal to 0, `b` is 0, `res` is the total number of iterations executed, which depends on the initial values of `a`, `b`, and `k`. If `a` was sufficiently large relative to `b` and `k`, then `res` counts how many times the loop could execute based on the decrement conditions applied to `a` and `b`.
    print(res)
#Overall this is what the function does:The function accepts four integer parameters: `k` (between 2 and 1000), `a` (a positive integer representing the number of nuts), `b` (a positive integer representing the number of divisors), and `v` (a positive integer representing the capacity of each section of the box). It calculates how many iterations it can perform in a loop that reduces the number of nuts `a` based on the values of `b` and `k`. The loop continues until `a` is less than or equal to 0, counting the number of iterations in `res`, which is then printed. The function does not return a value; it only prints the result.

