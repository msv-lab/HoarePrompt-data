#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 999,999, `a` is a list of 1000000 elements where all elements at indices that are not prime numbers starting from index 1 are set to False. All prime numbers remain True.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is at least 1, `a` is a list of 1000000 elements with only prime indices set to True, and the count of prime numbers between index 1 and `int(s) - 1` is printed for each `s` provided from `sys.stdin`
#Overall this is what the function does:The function `func` initializes a list `a` of 1000000 elements with all elements set to True. It then iterates over the range from 2 to 999,999 and marks non-prime indices in the list as False. After that, the function reads input from `sys.stdin`, converts it to an integer `s`, and prints the count of prime numbers between index 1 and `s - 1` from the list `a`. The function does not accept any parameters and does not have a specific return value.

