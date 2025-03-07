#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid folder names in the current directory where the digits in the folder name correspond to the range specified.
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
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: The loop has executed all its iterations. The variable `i` is equal to `t`, `t` remains unchanged, `a` is the last input string received, `count` is the number of '1's in `a`, and `n` is the last input integer received.
#Overall this is what the function does:The function processes multiple inputs, each consisting of an integer `n` followed by a string `a`. It counts the number of '1's in the string `a`. Based on the count, it prints either 'YES' or 'NO'. After processing all inputs, the function does not return anything.

