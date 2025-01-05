#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999; `a` is a list of 1000000 boolean values with elements set to True where the index is not a perfect square; `i` is 1000000. If `a[i - 1]` is True, then the program continues with the current state of variables `n`, `a`, and `i.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999; `a` is a list of 1000000 boolean values with elements set to True where the index is not a perfect square; `i` is 1000000, the loop has finished execution and all values have been printed as per the loop code.
#Overall this is what the function does:The function `func` initializes a list `a` of 1000000 boolean values with elements set to True, excluding indexes that are perfect squares. It then iterates through a range and updates the elements in `a` accordingly. The function reads input from standard input, iterates over the input values, and prints the count of True values in `a` up to the input value. The function does not explicitly return any value and operates within the constraints where `n` is an integer satisfying 1 ≤ n ≤ 999,999. The functionality is limited to processing inputs and printing results based on the content of list `a`.

