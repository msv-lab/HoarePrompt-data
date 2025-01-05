#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999, `a` is a list of 1000000 elements with elements at indices that are not perfect squares set to True and elements at perfect square indices set to False.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 999,999, `a` is a list of 1000000 elements with elements at indices that are not perfect squares set to True and elements at perfect square indices set to False, the count of True values in the sublist of `a` from index 1 to the square root of `n` (exclusive) is printed for each input `s` in `sys.stdin`
#Overall this is what the function does:The function `func` initializes a list `a` of 1000000 elements with True values. It then iterates over the range from 2 to 999,999, marking elements of the list `a` as False at indices that are perfect squares or multiples of prime numbers. After this process, it reads input values from `sys.stdin`, calculates the count of True values in the sublist of `a` from index 1 to the square root of each input value `s`, and prints this count. The function does not accept any parameters and does not return any value.

