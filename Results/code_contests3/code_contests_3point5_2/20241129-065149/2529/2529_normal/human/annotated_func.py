#State of the program right berfore the function call: m is a positive integer (1 ≤ m ≤ 200,000) and each jump coordinate is given in the form (a+b)/c where a, b, and c are positive integers of up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer, `test_list` contains `m` floating-point numbers, each appended value `e` is a floating-point number
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer, `test_list` contains `m` floating-point numbers, `my_list` contains the count of each unique number in `test_list`, `i` is the last number in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads a positive integer `m`, then reads `m` floating-point numbers and stores them in a list `test_list`. It then counts the occurrences of each unique number in `test_list` and stores the counts in a new list `my_list`. Finally, it prints the counts of each unique number in `test_list` as a space-separated string.

