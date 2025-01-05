#State of the program right berfore the function call: **Precondition**: 
- The input consists of m (1 ≤ m ≤ 200,000) ships.
- Each ship's jump coordinate is given as an arithmetic expression of the form (a+b)/c, where:
  - a and b are positive integers of up to two decimal digits.
  - c is a positive integer of up to two decimal digits.
def func():
    m = int(input())
    test_list = []
    for i in range(m):
        e = float(input())
        
        test_list.append(e)
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `i` is equal to `m-1`, `e` is the input floating-point number, `test_list` contains `m` elements of input floats
    my_list = []
    for i in test_list:
        my_list.append(test_list.count(i))
        
    #State of the program after the  for loop has been executed: `m` is greater than 0, `i` is equal to 0, `e` is the input floating-point number, test_list contains more than `m` elements of input floats, my_list is a list containing the count of occurrences of each element in test_list
    print(' '.join(map(str, my_list)))
#Overall this is what the function does:The function reads an integer m as input representing the number of ships. Each ship's jump coordinate, given in the form (a+b)/c, is then read as a floating-point number and added to a list test_list. Subsequently, the function counts the occurrences of each element in test_list and stores these counts in my_list. Finally, the function prints the counts as a string. The function essentially processes and displays the frequency of occurrence of jump coordinates for the given ships.

