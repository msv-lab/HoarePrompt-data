#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent the inclusive range of folder names to process.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: `start` is an integer, `end` is an integer, `t` must be exactly equal to the total number of iterations the loop has executed, `n` is an input integer, `s` is the value of the input string, `cnt1` is the number of '1's in the string `s`. The final state of `cnt1` depends on the conditions checked within the loop for each iteration. Specifically, if `cnt1` is greater than 2 and even, the output will be 'YES'. If `cnt1` is greater than 2 and odd, or `cnt1` is less than or equal to 2 or odd, the output will be 'NO'. Additionally, if the string `s` contains '11' at any point during the iterations, the output will be 'NO' for that iteration regardless of the value of `cnt1`.
    #
    #This means that after all iterations, the final value of `cnt1` will reflect the cumulative state of the condition checks performed on the input strings `s` throughout the loop. If any string `s` met the criteria for printing 'NO', the overall output will be 'NO'. Otherwise, if no string `s` met the 'NO' criteria, the final output will depend on the last `cnt1` value checked, which could be either 'YES' or 'NO' based on its parity and whether it was greater than 2.
#Overall this is what the function does:The function processes a series of input strings `s` based on their content and prints 'YES' or 'NO' accordingly. Specifically, it checks if the string `s` contains two consecutive '1's ('11'), if the count of '1's in the string is greater than 2 and even, or if the count of '1's is greater than 2 and odd. If any string `s` meets the criteria for 'NO', the function prints 'NO' and stops further processing. If no string `s` meets the 'NO' criteria, the function prints 'YES' based on the last checked string `s`.

