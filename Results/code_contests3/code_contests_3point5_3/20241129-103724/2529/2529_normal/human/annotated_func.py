#State of the program right berfore the function call: m is a positive integer representing the number of ships. Each jump coordinate is given in the form (a+b)/c where a, b, and c are positive integers with up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer, `test_list` contains `m` floats that have been inputted during the loop iterations
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer, `test_list` contains `m` floats, `my_list` contains the count of each float in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads in a positive integer m representing the number of ships, and then reads m float values into a list test_list. It then creates another list my_list that stores the count of each float in test_list. Finally, it prints the counts of each float in my_list separated by spaces. The function does not calculate or return the average jump coordinate as indicated in the comment.

