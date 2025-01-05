#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200000, and each ship's jump coordinate is given as a string in the format "(a+b)/c", where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer in the range [1, 200000]; `i` is `m - 1`; `test_list` contains `m` float elements that were inputted by the user.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer in the range [1, 200000]; `test_list` contains `m` float elements; `my_list` contains the count of occurrences of each element in `test_list`, with a length equal to `m`, reflecting the number of elements in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts a positive integer `m` (where 1 ≤ m ≤ 200000) as input, then reads `m` float values from user input and counts the occurrences of each float value in the list. Finally, it prints the counts of occurrences for each float in the same order as they were inputted. However, it does not process or validate any ship jump coordinates formatted as "(a+b)/c", which are mentioned in the annotations but not actually handled in the code.

