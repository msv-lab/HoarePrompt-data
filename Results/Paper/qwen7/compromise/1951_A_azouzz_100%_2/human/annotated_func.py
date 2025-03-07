#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end represent valid folder names in the current directory, where each folder name is a digit string.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2:
            print('NO')
        elif cnt1 == 1:
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' responses based on the conditions evaluated for each string `s` read from input during the loop iterations. Specifically, for each iteration, if the count of '1's in the string `s` is greater than 2 and even, it prints 'YES'. If the count of '1's is greater than 2 and odd, or if there are consecutive '1's ('11'), it prints 'NO'. Otherwise, if the count of '1's is exactly 1, it also prints 'NO'. The output will contain `t` such responses, one for each input string `s`.
#Overall this is what the function does:The function reads multiple integer inputs `t` and for each of these inputs, it reads a string `s`. It then checks the count of '1's in each string `s`. Based on the count and presence of consecutive '1's, it prints 'YES' or 'NO'. The function does not return any value; instead, it outputs a series of 'YES' or 'NO' responses corresponding to the input strings `s`.

