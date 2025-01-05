#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200,000, and each jump coordinate is a string formatted as "(a+b)/c" where a, b, and c are positive integers up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200,000; `test_list` contains `m` floating-point numbers; the last value appended to `test_list` is the last float input; `i` is `m - 1`.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200,000; `test_list` contains `m` floating-point numbers; `i` is the last floating-point number in `test_list`; `my_list` contains the counts of each floating-point number in `test_list`, with the length of `my_list` equal to `m`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m` (where 1 ≤ m ≤ 200,000) as input and then reads `m` floating-point numbers. It counts the occurrences of each number in the input list and prints these counts as space-separated values. The function does not process any specific jump coordinates as strings, and it may produce incorrect results if the same number appears multiple times, as it counts occurrences for each element within the input list. There is no return value from the function; it only outputs the counts directly to the console.

