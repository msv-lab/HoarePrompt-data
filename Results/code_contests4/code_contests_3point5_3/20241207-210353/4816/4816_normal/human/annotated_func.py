#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000, and NUMBERS is a list of integers where each element is between 1 and N, and all elements in NUMBERS are distinct.**
def func_1(N, NUMBERS):
    n = int(N)
    numbers = [int(s) for s in NUMBERS.split(' ')]
    sum = 0
    for num in numbers:
        sum += num
        
    #State of the program after the  for loop has been executed: NUMBERS is a list with at least 1 element, sum is the sum of all elements in the list, n is the value of the last element in the list
    sys.stdout.write(str(int(n * (n + 1) / 2 - sum)) + '\n')
#Overall this is what the function does:The function `func_1` takes two parameters, `N` and `NUMBERS`. `N` is converted to an integer, and `NUMBERS` is converted to a list of integers. The function calculates the sum of all elements in `NUMBERS`, then subtracts this sum from the sum of integers from 1 to `N`. The result is then printed to the console. The function does not explicitly return any value.

