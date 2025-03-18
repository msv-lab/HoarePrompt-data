#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
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
        
    #State: Output State: t is the number of iterations left, start and end remain unchanged, the output consists of 'YES' or 'NO' based on the conditions met within each iteration of the loop for the respective values of n and string a.
#Overall this is what the function does:The function processes a series of inputs, each consisting of an integer `t`, followed by `t` pairs of an integer `n` and a string `a`. For each pair, it checks if the string `a` contains exactly one '1' or more than two '1's with an even count. If the count of '1's is zero, exactly two, or meets the specific condition for more than two '1's, it prints 'YES'; otherwise, it prints 'NO'. The function does not modify any input parameters and outputs 'YES' or 'NO' for each input pair.

