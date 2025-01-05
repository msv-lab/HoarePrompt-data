#State of the program right berfore the function call: m is a positive integer representing the number of ships. Each jump coordinate expression is of the form (a+b)/c where a, b, and c are positive integers of up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is the total number of ships, `test_list` is a list containing all the float inputs entered during the loop execution
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is the total number of ships, `test_list` is a list containing all the float inputs entered during the loop execution, `my_list` contains the count of each element in `test_list`, `i` is the last element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function takes a positive integer `m` as input representing the number of ships. It then prompts the user to input `m` float numbers, stores them in a list `test_list`, and calculates the count of each element in `test_list`. Finally, it prints the counts of each element in `test_list` as a space-separated string.

