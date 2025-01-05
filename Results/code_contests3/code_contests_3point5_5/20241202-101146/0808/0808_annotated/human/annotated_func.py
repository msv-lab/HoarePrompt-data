#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` remains 999,999, `i` is 1000000, and `a` is an array with values set to False at indexes corresponding to non-prime numbers less than or equal to 999,999.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` remains 999,999, `i` is 1,000,000, and `a` is an array with values set to False at indexes corresponding to non-prime numbers less than or equal to 999,999.
#Overall this is what the function does:The function `func` initializes an array `a` of size 1000000 with all values set to True. It then iterates over a range of numbers and marks multiples of prime numbers as False in the array. The function reads input from `sys.stdin`, converts it to an integer, and prints the count of True values in the array up to that integer. The function does not accept any parameters and does not return any value.

