#State of the program right berfore the function call: n is an integer greater than or equal to 2.
def func():
    n = int(raw_input())
    count = n
    while n != 1:
        for i in range(2, n):
            if divmod(n, i)[1] == 0:
                break
        
        b = n // i
        
        count += b
        
        n -= b
        
        if b == 1:
            break
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of initial `n` and all values of `b` computed during the iterations until `n` became 1.
    print(count)
#Overall this is what the function does:The function accepts an integer `n` greater than or equal to 2, continuously divides `n` by the smallest integer that divides `n` evenly, and accumulates the results in `count`. The process continues until `n` becomes 1, at which point it prints the total count, which includes the initial value of `n` and all computed divisions.

