#State of the program right berfore the function call: The input consists of several datasets, each containing an integer n such that 1 <= n <= 999,999. The number of datasets is less than or equal to 30.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements, where elements at prime indices are True and non-prime indices are False.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where elements at prime indices are True and non-prime indices are False; the count of True values in the slice a[1:int(s)] is printed for each input value from sys.stdin.
#Overall this is what the function does:The function accepts multiple integer inputs (each between 1 and 999,999) and counts the number of prime numbers up to each input value. It uses a sieve algorithm to precompute which numbers are prime and prints the count of prime numbers for each input. If an input value is less than 1 or greater than 999,999, it may lead to an error since the code does not explicitly handle these edge cases.

