#State of the program right berfore the function call: m is a positive integer such that 1 ≤ m ≤ 200,000, and each jump coordinate is a valid arithmetic expression of the form (a+b)/c, where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is a positive integer such that 1 ≤ `m` ≤ 200,000; `test_list` contains `m` floating-point inputs.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is a positive integer such that 1 ≤ `m` ≤ 200,000; `my_list` contains the counts of occurrences of each unique element in `test_list`, with each count corresponding to the respective element from `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts a positive integer `m` (1 ≤ m ≤ 200,000) representing the number of subsequent floating-point inputs. It then reads `m` floating-point numbers from the input and counts the occurrences of each unique number in that list, returning a space-separated string of these counts corresponding to the order of the original inputs. The function does not handle edge cases such as invalid input types or values outside the specified range.

