#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200,000, and each jump coordinate is a string in the format "(a+b)/c" where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200,000, `i` is `m - 1`, `e` is the last float input, and `test_list` contains `m` float values.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200,000; `test_list` contains `m` float values; `my_list` contains the counts of each unique value in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer input `m` (1 ≤ m ≤ 200,000) representing the number of float values to be inputted. It then reads `m` float values from the user, counts the occurrences of each float value in the list, and prints these counts as space-separated strings. The function does not handle edge cases for invalid input formats or values outside the specified range; it assumes that all inputs will be valid according to the given constraints.

