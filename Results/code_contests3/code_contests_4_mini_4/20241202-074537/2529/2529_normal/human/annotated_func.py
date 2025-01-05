#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200,000, and each of the next m lines contains a valid arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an integer such that 1 ≤ `m` ≤ 200,000; `test_list` contains `m` floating-point numbers obtained from input, and `i` is equal to `m - 1`.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is an integer such that 1 ≤ `m` ≤ 200,000; `test_list` contains `m` floating-point numbers; `my_list` contains the counts of each element in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m` representing the number of arithmetic expressions to be processed, reads `m` floating-point numbers from input, counts the occurrences of each floating-point number in the list, and prints these counts as a space-separated string. The function does not evaluate any arithmetic expressions; instead, it simply counts and outputs the frequency of each number in the input list.

