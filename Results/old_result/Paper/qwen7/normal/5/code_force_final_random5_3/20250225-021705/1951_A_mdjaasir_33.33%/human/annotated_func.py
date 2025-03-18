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
        
    #State: `start` is an integer, `end` is an integer such that `start` <= `end`, `t` is an input integer that must be at least 1, `i` is `t`, `n` is an input integer, `a` is an input string, and `count` is the number of '1's in the string `a`. The value of `count` will depend on the input strings `a` provided during each iteration of the loop. If `count` is 0, the condition remains unchanged. If `count` is greater than 2 and even, the condition remains unchanged. Otherwise, `count` remains unchanged.
#Overall this is what the function does:The function processes multiple input strings `a` and checks the count of '1's within each string. Based on the count, it prints 'YES' or 'NO' for each string. The function does not accept any parameters and does not return anything.

