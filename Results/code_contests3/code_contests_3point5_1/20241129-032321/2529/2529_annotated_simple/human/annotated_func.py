#State of the program right berfore the function call: 
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains the floats entered during each iteration, `i` is equal to `m - 1`, `e` is the input float for the last iteration
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains floats, `i` is the last float in `test_list`, `e` is the input float for the last iteration, `my_list` contains the count of each float in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads an integer `m` from the user, then reads `m` floating-point numbers into a list `test_list`. It then iterates over each element in `test_list`, counts the occurrences of each element, and stores the counts in a new list `my_list`. Finally, it prints the counts of each unique float in `test_list` separated by spaces. The function does not accept any parameters and does not return any value.

