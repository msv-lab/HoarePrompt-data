#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200000, and each jump coordinate is an arithmetic expression of the form (a+b)/c where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is the input integer, `i` is equal to `m`, `test_list` contains `m` floating-point numbers inputted by the user.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is the input integer, `i` is equal to the last floating-point number in `test_list`, `my_list` contains the counts of each floating-point number in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts no parameters and processes a positive integer `m` (where 1 ≤ m ≤ 200000) representing the number of floating-point numbers to be inputted by the user. It collects these numbers into a list and then generates a new list containing the count of each number's occurrences in the original list. Finally, it prints these counts as a space-separated string. The function does not validate the input format for floating-point numbers, which could lead to errors if the user enters invalid data.

