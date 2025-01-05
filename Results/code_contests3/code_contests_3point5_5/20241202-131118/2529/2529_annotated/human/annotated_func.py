#State of the program right berfore the function call: **
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains `m` elements each equal to a floating-point number entered as input
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains `m` elements, `my_list` contains the count of each unique element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads an integer `m` from the user, then reads `m` floating-point numbers and stores them in a list `test_list`. It then counts the occurrences of each unique element in `test_list` and prints the counts separated by spaces. The function does not accept any parameters and returns the counts of unique elements in the input list.

