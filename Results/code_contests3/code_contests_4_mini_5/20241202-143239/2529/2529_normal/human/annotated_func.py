#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200000, and each jump coordinate is a string in the format "(a+b)/c" where a, b, and c are positive integers of up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is between 1 and 200000; `test_list` contains `m` floating-point numbers from input.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is between 1 and 200000, `test_list` contains `m` floating-point numbers, `i` is each floating-point number in `test_list` during the iterations, `my_list` contains the counts of each floating-point number in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m` (1 ≤ m ≤ 200000), and then it reads `m` floating-point numbers from input, storing them in a list called `test_list`. It counts the occurrences of each floating-point number in `test_list` and stores these counts in another list called `my_list`. Finally, it prints the counts of each number in `my_list` as a space-separated string. The function does not handle the input format "(a+b)/c" stated in the annotations and focuses solely on counting the occurrences of the floating-point numbers provided.

