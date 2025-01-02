#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999, `a` is a list of 1,000,000 boolean values where `a[0]` and `a[1]` are `True`, and for each index `i` from 2 to 999,999, `a[i]` is `True` if and only if `i` is a prime number. All other indices are set to `False`.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999, `a` is a list of 1,000,000 boolean values where `a[0]` and `a[1]` are `True`, and for each index `i` from 2 to 999,999, `a[i]` is `True` if and only if `i` is a prime number. All other indices are set to `False`. `sys.stdin` must have contained at least one line of input for each iteration of the loop. The number of `True` values from index 1 to `int(s) - 1` in the list `a` has been printed for each line of input. If `sys.stdin` was empty, no output is produced and the list `a` remains unchanged.
#Overall this is what the function does:The function `func()` initializes a list `a` of 1,000,000 boolean values, where initially all values are set to `True`. It then iterates through the list starting from index 2 (representing the number 2), marking non-prime numbers as `False`. After this, the function reads lines from `sys.stdin`, and for each line, it prints the count of prime numbers (represented by `True` values) from 1 up to the integer value read from the input. The function does not explicitly accept any parameters and does not return any value. The final state of the program is that `a` is a list where `a[0]` and `a[1]` are `True`, and for each index `i` from 2 to 999,999, `a[i]` is `True` if and only if `i` is a prime number. All other indices are set to `False`. If `sys.stdin` is empty, no output is produced, and the list `a` remains unchanged.

