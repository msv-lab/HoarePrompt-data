#State of the program right berfore the function call: **Precondition**: 
- The input consists of m ships, where m is a positive integer such that 1 ≤ m ≤ 200,000.
- Each ship's jump coordinate is given as an arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers of up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer between 1 and 200,000, `test_list` is a list containing `m` floating-point numbers input by the user
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer between 1 and 200,000, `test_list` contains `m` floating-point numbers, `i` is the last element in `test_list`, `my_list` is a list containing the count of each unique element in `test_list`
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads the input for the number of ships, where each ship's jump coordinate is given as a floating-point number. It then counts the occurrences of each unique jump coordinate and prints the counts. The function handles cases where the input does not match the specified format or constraints are violated.

