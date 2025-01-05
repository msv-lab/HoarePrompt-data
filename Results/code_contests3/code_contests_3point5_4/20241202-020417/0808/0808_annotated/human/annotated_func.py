#State of the program right berfore the function call: n is an integer such that 1 <= n <= 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 999,999, `a` is a list of 1000000 True values except for the indexes that are multiples of prime numbers greater than 2, all these indexes will be False, `i` is 1000000, all indexes `a[j]` are False for all j such that j is a multiple of a prime number greater than 2
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: The loop will continue to read integers from sys.stdin and print the count of True values in the list `a` from index 1 to that integer. It will keep executing until there are no more elements in the standard input.
#Overall this is what the function does:The function `func` initializes a list of 1000000 True values and then updates certain indexes to False based on prime numbers. It reads integers from the standard input and prints the count of True values in the list `a` from index 1 to the read integer. The function does not accept any parameters and does not explicitly return any output.

