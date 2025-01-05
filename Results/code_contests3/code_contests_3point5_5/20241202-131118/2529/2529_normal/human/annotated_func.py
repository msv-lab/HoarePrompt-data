#State of the program right berfore the function call: **
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains `m` floating-point numbers inputted by the user
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains `m` elements, `my_list` contains the count of each unique element in `test_list`, `i` is the last element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads an integer `m` from the user, then reads `m` floating-point numbers to create a list `test_list`. It then iterates over `test_list` to count the occurrences of each unique element and store them in a new list `my_list`. Finally, it prints the counts of each unique element in `test_list` separated by spaces. The function does not accept any parameters and simply executes the described process.

