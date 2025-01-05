#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is not a prime number, all elements in list `a` up to index 1000000 are False, indicating non-prime numbers.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: The loop will continue to read integers from sys.stdin and print the count of True values in list `a` from index 1 to the integer value read from sys.stdin. Since the loop does not have a termination condition, it will continue indefinitely or until the program is interrupted.
#Overall this is what the function does:The function `func` initializes a list `a` of size 1000000 with all elements set to True. It then iterates through the list to mark non-prime numbers as False based on the Sieve of Eratosthenes algorithm. After that, the function enters an infinite loop reading integers from `sys.stdin` and prints the count of True values in list `a` up to the integer read. The loop continues indefinitely until interrupted. The function does not accept any parameters and its output is not specified.

