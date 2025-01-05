#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200,000, and each jump coordinate is a string formatted as (a+b)/c where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer such that 1 ≤ `m` ≤ 200,000; `i` is `m - 1`; `test_list` contains `m` floating-point numbers from input.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer such that 1 ≤ `m` ≤ 200,000; `test_list` is a list containing `m` floating-point numbers; `my_list` contains counts of occurrences of each corresponding floating-point number in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts a positive integer `m` (1 ≤ m ≤ 200,000) and reads `m` floating-point numbers from input. It counts the occurrences of each number in the list and prints these counts as a space-separated string. The function does not handle invalid input formats or any conditions related to the string formatted as (a+b)/c, and it assumes all inputs are valid floating-point numbers.

