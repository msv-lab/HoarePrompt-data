#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 999,999, all elements of list `a` are `True` except for elements from index 2 to 999,999 which are `False`
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: n is an integer such that 1 <= n <= 999,999, all elements of list a are True except for elements from index 2 to 999,999 which are False, the count of True values in a from index 1 to n-1 is equal to n-1
#Overall this is what the function does:The function `func` initializes a list `a` with True values, then iterates over a range and marks multiples of numbers as False in the list. It reads input from `sys.stdin`, prints the count of True values in the list `a` up to a specified index, excluding that index. The function does not accept any parameters and does not return any value.

