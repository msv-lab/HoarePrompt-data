#State of the program right berfore the function call: N is an integer such that 2 <= N <= 100000. NUMBERS is a list of integers with length N-1, where each element is an integer between 1 and N, inclusive, and all elements are distinct.**
def func_1(N, NUMBERS):
    n = int(N)
    numbers = [int(s) for s in NUMBERS.split(' ')]
    sum = 0
    for num in numbers:
        sum += num
        
    #State of the program after the  for loop has been executed: N is an integer such that 2 <= N <= 100000, NUMBERS is a list of integers with length N-1, where each element is an integer between 1 and N, inclusive, and all elements are distinct; n is an integer between 2 and 100000, sum is the sum of all elements in the NUMBERS list
    sys.stdout.write(str(int(n * (n + 1) / 2 - sum)) + '\n')
#Overall this is what the function does:The function `func_1` takes two parameters: `N`, an integer where 2 <= N <= 100000, and `NUMBERS`, a list of integers with length N-1, where each element is an integer between 1 and N, inclusive, and all elements are distinct. The function calculates the sum of all elements in the NUMBERS list, subtracts it from the sum of integers from 1 to N, and prints the result. The function does not explicitly return any value.

