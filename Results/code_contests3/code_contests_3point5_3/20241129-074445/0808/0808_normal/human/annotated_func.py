#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999, `a` is a list of 1000000 boolean values with all elements set to `False`, and `i` is 1000000. All elements in `a` that are multiples of prime numbers up to 1000000 have been set to `False`.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the program will print the count of `True` values in `a` from index 1 to the last value of `s` provided by `sys.stdin` for each iteration.
#Overall this is what the function does:The function `func` initializes a list `a` of 1000000 boolean values all set to True. It then iterates over the range from 2 to 999,999, setting elements in `a` to False if they are multiples of prime numbers up to 999,999. However, the function does not accept any parameters and does not have a return value. Additionally, the function reads input from `sys.stdin` and prints the count of True values in `a` from index 1 to the last value of each input provided.

