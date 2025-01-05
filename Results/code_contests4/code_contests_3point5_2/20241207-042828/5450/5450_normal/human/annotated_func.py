#State of the program right berfore the function call: A and B are positive integers such that 1 <= A <= B <= 20.**
def func():
    list = [int(i) for i in raw_input().split()]
    if (list[1] % list[0] == 0) :
        print(list[0] + list[1])
    else :
        print(list[1] - list[0])
    #State of the program after the if-else block has been executed: *A and B are positive integers such that 1 <= A <= B <= 20, list contains the input integers converted to integers. If the second element of the list is divisible by the first element, the sum of the first and second elements is returned. Otherwise, the difference between the second element and the first element of the list is printed.
#Overall this is what the function does:The function `func` reads two integers from the user input and checks if the second integer is divisible by the first integer. If it is divisible, it prints the sum of the two integers; otherwise, it prints the difference between the second and first integer. The function operates based on the constraints of positive integers A and B where 1 <= A <= B <= 20. The function does not explicitly return any value.

