#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names in the current working directory (obtained using `os.getcwd()`), where each directory name is a digit string.
def func():
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' printed based on the conditions inside the loop for each iteration where `t` is greater than 0.
    #
    #Explanation: For each iteration of the loop, the value of `t` is decremented by 1. Inside the loop, the program reads two inputs: an integer `n` and a string `s`. Based on the value of `n`, it checks specific conditions and prints either 'YES' or 'NO'. If `n` is 2, it checks if `s` is '00'; if so, it prints 'YES', otherwise 'NO'. If `n` is not 2, it counts the number of '1's in `s`. If the count of '1's is odd or there is exactly one occurrence of '11', it prints 'NO', otherwise it prints 'YES'. This process repeats until `t` becomes 0.
#Overall this is what the function does:The function processes a series of inputs, each consisting of an integer `n` and a string `s`. It prints 'YES' or 'NO' based on specific conditions related to the value of `n` and the content of `s`. If `n` is 2, it checks if `s` equals '00'. Otherwise, it counts the number of '1's in `s` and checks if the count is even and if there are no two consecutive '1's. The function does not return any value; it only prints the results of its checks.

