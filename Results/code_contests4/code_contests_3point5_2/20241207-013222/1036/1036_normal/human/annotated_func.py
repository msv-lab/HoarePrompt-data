#State of the program right berfore the function call: n is an integer such that 2 <= n <= 10^9.**
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
        
    #State of the program after the loop has been executed: If the final value of `n` is a prime number, `count` is updated accordingly. The final values of `n` and `count` depend on the prime factorization of the initial `n` value.
    print(count)
#Overall this is what the function does:The function `func` reads an integer `n` from the user, calculates the sum of its prime factors, and prints the resulting count. The final count value depends on the prime factorization of the input `n`. The function does not accept any parameters and does not return any value.

