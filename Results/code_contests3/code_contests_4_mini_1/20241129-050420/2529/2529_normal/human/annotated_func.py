#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200,000, and each jump coordinate is a string formatted as (a+b)/c, where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an input integer between 1 and 200,000; `test_list` contains `m` floating-point numbers input by the user.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `my_list` contains the counts of occurrences of each unique element in `test_list`, `m` is an input integer between 1 and 200,000, and `test_list` contains `m` floating-point numbers input by the user.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts no parameters and reads an integer `m` from input, which specifies the number of subsequent floating-point numbers to read. It stores these numbers in a list and then counts the occurrences of each unique number in that list. Finally, it prints the counts of each number as a space-separated string. The function does not handle any edge cases related to input validation beyond the assumptions made about `m`. It also does not process any jump coordinates formatted as (a+b)/c, as suggested by the annotations; instead, it simply counts and displays occurrences of floating-point numbers.

