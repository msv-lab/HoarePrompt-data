#State of the program right berfore the function call: x_1, x_2, x_3, and x_4 are four positive integers such that 2 ≤ x_i ≤ 10^9.
def func():
    numbers = [int(x) for x in raw_input().split()]
    numbers.sort()
    print('{0} {1} {2}'.format(numbers[3] - numbers[0], numbers[3] - numbers[1],
    numbers[3] - numbers[2]))
#Overall this is what the function does:The function accepts four positive integers from user input, sorts them, and prints the differences between the largest integer and each of the three smaller integers. Specifically, it returns the differences between the largest number and the second, third, and fourth largest numbers, respectively. It does not explicitly handle cases where fewer or more than four integers are provided.

