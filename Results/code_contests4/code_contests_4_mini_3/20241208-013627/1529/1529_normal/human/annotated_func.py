#State of the program right berfore the function call: x_1, x_2, x_3, and x_4 are four positive integers such that 2 ≤ x_i ≤ 10^9 for i in {1, 2, 3, 4}.
def func():
    numbers = [int(x) for x in raw_input().split()]
    numbers.sort()
    print('{0} {1} {2}'.format(numbers[3] - numbers[0], numbers[3] - numbers[1],
    numbers[3] - numbers[2]))
#Overall this is what the function does:The function accepts four positive integers (x_1, x_2, x_3, and x_4) from user input, sorts them, and then computes and prints the differences between the largest number and each of the other three numbers. It does not return any value. The output will be three integers representing these differences.

