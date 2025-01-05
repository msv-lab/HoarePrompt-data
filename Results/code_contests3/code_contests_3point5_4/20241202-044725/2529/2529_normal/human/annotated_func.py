#State of the program right berfore the function call: m is a positive integer less than or equal to 200,000. Each jump coordinate expression follows the format (a+b)/c where a, b, and c are positive integers of up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains all the values of `e` appended in each iteration of the loop, `i` is equal to `m`, `e` is the last input floating-point number
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is the last value in `test_list`, `test_list` is not empty, `e` is equal to `m`, `i` is equal to `m`, `my_list` contains the count of occurrences of each element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads a positive integer `m`, then reads `m` floating-point numbers and stores them in a list `test_list`. It then counts the occurrences of each element in `test_list` and stores the counts in a new list `my_list`. Finally, it prints the counts as space-separated values. The function generates jump coordinates based on the given constraints of positive integers up to two decimal digits.

