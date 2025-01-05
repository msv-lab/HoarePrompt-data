#State of the program right berfore the function call: m is a positive integer (1 ≤ m ≤ 200,000) and each jump coordinate expression is of the form (a+b)/c where a, b, and c are positive integers of up to two decimal digits.**
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: m is a positive integer, test_list contains m input float values, i is m-1
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: m is a positive integer, test_list contains m float values, i is m, my_list contains the count of occurrences of each value in test_list
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function `func` reads a positive integer `m`, then reads `m` float values, and calculates the count of occurrences of each value in the input list. Finally, it prints the counts as a space-separated string. The code does not calculate jump coordinates as mentioned in the annotations.

