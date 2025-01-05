#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 999,999, `a` contains 1000000 elements with only prime indices set to `True` and all other elements set to `False`, `i` is 1000000. If the element at index `i - 1` (prime index) is `True`, then the program continues. Otherwise, the program exits without further changes.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 999,999, `a` contains 1000000 elements with only prime indices set to `True`, all other elements set to `False`, `i` is 1000000, the element at index i - 1 in list 'a' is True for the loop to execute. The code prints the count of True values in list `a` from index 1 to `n-1`.
#Overall this is what the function does:The function initializes a list `a` of 1000000 elements with all values set to True. It then iterates over the range from 2 to 999,999 and marks non-prime indices in the list `a` as False based on the Sieve of Eratosthenes algorithm. After that, it attempts to read input from the standard input and prints the count of True values in the list `a` from index 1 to n-1 for each input line. The function does not accept any parameters and does not return any value.

