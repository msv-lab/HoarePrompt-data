#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000. NUMBERS is a list of integers where each integer is between 1 and N, and the length of NUMBERS is N-1.**
def func_1(N, NUMBERS):
    n = int(N)
    numbers = [int(s) for s in NUMBERS.split(' ')]
    sum = 0
    for num in numbers:
        sum += num
        
    #State of the program after the  for loop has been executed: `N` is an integer, `NUMBERS` is a list of integers, `sum` is the sum of all integers in the list `NUMBERS`, `num` is the last integer in the list
    sys.stdout.write(str(int(n * (n + 1) / 2 - sum)) + '\n')
#Overall this is what the function does:The function `func_1` accepts two parameters: `N`, an integer within the range 2 to 100000, and `NUMBERS`, a list of integers where each integer falls between 1 and N, with the length of `NUMBERS` being N-1. The function calculates the sum of integers in the `NUMBERS` list, subtracts it from the sum of integers from 1 to N, and outputs the result.

