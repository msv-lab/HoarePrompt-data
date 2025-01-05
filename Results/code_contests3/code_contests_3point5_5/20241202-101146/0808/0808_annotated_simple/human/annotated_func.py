#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 999,999, `a` is a list of 1000000 elements where all non-prime numbers are set to False, `i` is 1000000, and `j` is the next value that satisfies the loop condition within the range `i`.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: The loop will continue to read values from sys.stdin and print the count of True values in the sublist of `a` from index 1 to the integer value of `s` until there are no more values to read. `n`, `a`, `i`, and `j` will remain unchanged.
#Overall this is what the function does:The function initializes a list of 1000000 elements where all non-prime numbers are set to False using the Sieve of Eratosthenes algorithm. Then, it reads input values from sys.stdin, prints the count of True values in a sublist of the list `a` until there are no more values to read. The function does not accept any parameters.

