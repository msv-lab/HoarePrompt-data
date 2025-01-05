#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is 999,999, `a` is a list of 1000000 elements where the element at index 2 is True and all elements at indices that are multiples of a prime number starting from 3 are False. All other elements are False. The values of `i` and `j` are undefined after the execution of the loop
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is 999,999, `a` is a list of 1000000 elements with specific True and False values, `s` is being read from `sys.stdin`, the loop will continue to read input from `sys.stdin` but not print anything
#Overall this is what the function does:The function `func` initializes a list of 1000000 elements with True values, marks multiples of prime numbers as False, and then reads input from `sys.stdin`, calculates the count of True values in a slice of the list, but does not print the count. The function does not accept any parameters and does not return any value.

