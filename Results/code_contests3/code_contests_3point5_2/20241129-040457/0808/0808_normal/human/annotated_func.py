#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: n is an integer such that 1 ≤ n ≤ 999,999, a is a list of 1000000 elements with non-prime indices set to False, i is 1000000
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: n is an integer such that 1 ≤ n ≤ 999,999, a is a list of 1000000 elements with non-prime indices set to False, i is 1000000
#Overall this is what the function does:The function `func` initializes a list of 1000000 elements with all values set to True, then iterates over the list to mark non-prime indices as False following a specific algorithm. After that, it reads input from the standard input and prints the count of True values in the sublist of `a` from index 1 to the input value. The function does not accept any parameters and does not return anything.

