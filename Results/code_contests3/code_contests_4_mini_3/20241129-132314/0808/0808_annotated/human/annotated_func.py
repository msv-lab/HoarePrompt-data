#State of the program right berfore the function call: The function reads multiple datasets consisting of integers n, where each n is a positive integer such that 1 ≤ n ≤ 999,999, and there are no more than 30 datasets.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 boolean values, where `True` represents prime indices and `False` represents non-prime indices.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 boolean values; `s` is the last line read from sys.stdin; the count of `True` values in the slice `a[1:int(s)]` is printed for each valid input line from sys.stdin.
#Overall this is what the function does:The function reads multiple datasets consisting of positive integers \( n \) (with \( 1 \leq n \leq 999,999 \)) from standard input and counts the number of prime numbers less than or equal to each \( n \). It prints the count for each input. The function does not handle cases where the input may be invalid (e.g., non-integer values or out-of-bounds integers), and it assumes that the input will always be valid and within the specified range.

