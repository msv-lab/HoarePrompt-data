#State of the program right berfore the function call: m is a positive integer and each jump coordinate expression follows the format (a+b)/c where a, b, and c are positive integers of up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `i` is equal to `m-1`, `e` is an input floating-point number, `test_list` contains `m` elements, each element being an input floating-point number
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `i` is the last element in `test_list`, `e` is the same as the last element in `test_list`, `my_list` contains the count of occurrences of each element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads a positive integer `m` from the input, then reads `m` floating-point numbers into a list `test_list`. After that, it counts the occurrences of each element in `test_list` and prints the counts as space-separated values. The function does not accept any parameters.

