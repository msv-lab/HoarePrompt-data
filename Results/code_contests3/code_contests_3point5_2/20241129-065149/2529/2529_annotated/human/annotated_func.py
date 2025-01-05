#State of the program right berfore the function call: **Precondition**: 
- m is a positive integer such that 1 <= m <= 200,000.
- Each jump coordinate expression is of the form (a+b)/c where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is the input integer, `test_list` contains the values entered during each iteration of the loop, `i` is `m-1`, `e` is the last float entered via input. If `m` is 0, `test_list` remains empty.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `test_list` has at least `m` elements, `i` is the last element of `test_list`, `e` is the last float entered via input, `my_list` contains the count of each element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads an integer `m` from the input and then reads `m` floating-point numbers. It stores these numbers in a list `test_list`. It then creates a new list `my_list` that contains the count of occurrences of each element in `test_list`. Finally, it prints the counts of each element in `test_list` separated by spaces. The function does not return any value.

