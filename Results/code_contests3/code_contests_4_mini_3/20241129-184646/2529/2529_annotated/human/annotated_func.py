#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200,000, and each of the next m lines contains a valid arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer such that 1 ≤ `m` ≤ 200,000; `i` is `m - 1`; `test_list` contains `m` floating-point numbers based on user input.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer such that 1 ≤ `m` ≤ 200,000; `my_list` contains the counts of each element in `test_list`, with a length of `m`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts no parameters, reads `m` floating-point numbers from user input, counts the occurrences of each number, and prints these counts as a space-separated string. It does not evaluate any arithmetic expressions.

