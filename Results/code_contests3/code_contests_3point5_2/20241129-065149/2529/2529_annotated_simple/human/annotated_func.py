#State of the program right berfore the function call: **Precondition**: 
- The input consists of m ships where 1 <= m <= 200,000.
- Each ship's jump coordinate is given as an arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers of up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains `m` floating-point numbers entered by the user, `e` is the last floating-point number entered by the user
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` contains `m` floating-point numbers entered by the user, `e` is the last floating-point number entered by the user, `my_list` contains the count of occurrences of each element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads an integer `m` representing the number of ships, then reads `m` floating-point numbers as jump coordinates for each ship. It then counts the occurrences of each unique jump coordinate in the input list and prints the count of occurrences for each unique jump coordinate. The function does not have any return value.

