#State of the program right berfore the function call: m is a positive integer (1 ≤ m ≤ 200,000), and each jump coordinate is a string in the form '(a+b)/c' where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer (1 ≤ m ≤ 200,000), `test_list` is a list containing `m` floating-point numbers inputted during the loop execution.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `my_list` contains the counts of each element in `test_list`, and `m` is a positive integer (1 ≤ m ≤ 200,000); `test_list` is a non-empty list.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m`, reads `m` floating-point numbers from user input, counts the occurrences of each number, and prints the counts as a space-separated string.

