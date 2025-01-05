#State of the program right berfore the function call: m is an integer such that 1 ≤ m ≤ 200000, and each ship's jump coordinate is given as a string in the format "(a+b)/c" where a, b, and c are positive integers with up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is an input integer within the range 1 to 200000; `test_list` contains `m` float inputs; `i` is equal to `m` after the loop completes.
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is an input integer within the range 1 to 200000, `test_list` contains `m` float inputs, `i` is equal to the last float in `test_list`, `my_list` is a list containing the counts of each float in `test_list`, where each count corresponds to the number of occurrences of the respective float in `test_list`.
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function accepts an integer `m` (1 ≤ m ≤ 200000) and reads `m` float values from input. It counts the occurrences of each float in the list and returns a space-separated string of these counts. The function does not process any ship jump coordinates as described in the annotations, and it assumes valid float inputs are provided.

