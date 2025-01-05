#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200000, and each jump coordinate is an arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200000; `i` is `m`; `test_list` contains `m` floating-point numbers from input.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200000; `test_list` is a list of floating-point numbers; `my_list` contains the counts of each unique floating-point number in `test_list`, where each count corresponds to the frequency of that number in `test_list`; `i` is the last floating-point number from `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m` (where 1 ≤ m ≤ 200000) and reads `m` floating-point numbers from input. It then counts the occurrences of each unique floating-point number in the input list. Finally, it prints these counts as a space-separated string. The function does not validate the input for the arithmetic expressions specified in the comments.

