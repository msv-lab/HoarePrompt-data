#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 999,999.**
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `n` is an integer in the range of 1 to 999,999; `a` is a list of 1,000,000 elements where the values are updated based on the prime number pattern; `i` is 1,000,000. After the execution of the loop, all elements in `a` that are not prime numbers will be set to False.
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `n` is an integer in the range of 1 to 999,999, `a` is a list of 1,000,000 elements where the non-prime numbers have been set to False, `i` is 1,000,000, no more input from `sys.stdin`
#Overall this is what the function does:The function initializes a list of 1,000,000 elements with True values and then updates the list based on a prime number pattern. It reads input from sys.stdin, prints the count of True values in the list up to a given input value, and repeats this process until there is no more input. The function does not accept any parameters and does not return any value.

