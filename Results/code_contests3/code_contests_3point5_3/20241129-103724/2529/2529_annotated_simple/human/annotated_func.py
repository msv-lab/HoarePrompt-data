#State of the program right berfore the function call: m is a positive integer representing the number of ships. Each jump coordinate is given as an arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers of up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: m is a positive integer representing the number of ships, test_list is a list containing the float values of all inputs, i is equal to m - 1, e is assigned the float value of the input
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than or equal to 1, `i` is the last element in `test_list`, `e` is the last element of `test_list`, `my_list` contains the count of each unique element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads a positive integer `m` representing the number of ships. It then reads `m` float values as input and stores them in a list `test_list`. Next, it creates a new list `my_list` where each element represents the count of occurrences of the corresponding element in `test_list`. Finally, it prints the counts of each unique element in `test_list` separated by spaces. The function does not accept any parameters explicitly.

