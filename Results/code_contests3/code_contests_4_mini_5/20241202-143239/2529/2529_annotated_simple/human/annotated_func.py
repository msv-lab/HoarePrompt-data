#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200000, and each of the next m lines contains a valid arithmetic expression of the form (a+b)/c where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer in the range 1 to 200000; `i` is `m - 1`; `test_list` contains `m` float values input from the user.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer in the range 1 to 200000; `test_list` contains `m` float values input from the user; `my_list` contains `m` integers representing the count of occurrences of each corresponding element in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts input from the user, where the first line indicates the number of subsequent arithmetic expressions (m), and the following m lines contain floating-point numbers. It counts the occurrences of each floating-point number from the input and prints these counts as a space-separated string. It does not perform any arithmetic calculations based on the input expressions, despite the initial comments suggesting it does.

