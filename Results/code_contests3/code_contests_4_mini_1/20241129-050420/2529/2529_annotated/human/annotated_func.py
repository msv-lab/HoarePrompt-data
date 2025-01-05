#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200000, and each of the subsequent m lines contains a valid arithmetic expression of the form (a+b)/c where a, b, and c are positive integers represented with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200000; `i` is `m - 1`; `e` is the last floating-point number input; `test_list` contains `m` floating-point numbers from the input.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is an input integer such that 1 ≤ `m` ≤ 200000; `my_list` contains the counts of each element in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m` from user input, which represents the number of subsequent lines containing valid floating-point numbers. It collects these numbers into a list and then counts the occurrences of each number in the list. Finally, it prints the counts of each number corresponding to their order of appearance, separated by spaces. However, the function does not evaluate any arithmetic expressions as suggested by the comments. Instead, it simply counts and displays the frequency of each input number.

