#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is 999,999, `a` is a list of 1000000 boolean values with the first two elements being True (representing prime numbers) and the rest being False (representing non-prime numbers).
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is 999,999, `a` is a list of 1000000 boolean values with the first two elements being True and the rest being False
#Overall this is what the function does:The function `func` initializes a list of 1000000 boolean values where the first two elements are True (representing prime numbers) and the rest are False (non-prime numbers). It then iterates through the list, marking multiples of each prime number as False. The function reads input from `sys.stdin` and prints the count of True values in the list up to the specified index. The function does not explicitly return any value and operates independently of external input.

