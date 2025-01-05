#State of the program right berfore the function call: m is a positive integer representing the number of ships. Each jump coordinate expression is of the form (a+b)/c where a, b, and c are positive integers with up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer representing the number of ships, `test_list` contains `m` float values inputted one by one, `i` is `m-1`, `e` is the last input float value
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer representing the number of ships, `test_list` contains `m` float values, `i` is `m-1`, `e` is the last input float value, `my_list` contains the count of occurrences of each unique value in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads a positive integer `m` representing the number of ships. It then prompts the user to input `m` float values, storing them in a list `test_list`. After that, it iterates through `test_list` to count the occurrences of each unique value and stores these counts in a list `my_list`. Finally, it prints the counts of unique values in `test_list` separated by spaces.

