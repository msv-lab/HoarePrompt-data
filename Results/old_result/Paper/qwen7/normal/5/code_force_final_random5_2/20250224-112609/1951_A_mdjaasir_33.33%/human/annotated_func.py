#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading zeros.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: i is 3, t must be greater than 0, n is an input integer, a is the value entered by the user as a string, count is the number of '1's in the string a. The postcondition remains the same as the precondition regardless of whether the condition count == 0 is true or false.
#Overall this is what the function does:The function processes multiple inputs, counting the occurrences of the digit '1' in each input string. Based on the count, it prints 'YES' or 'NO' for each input. The function does not accept any parameters and does not return anything.

