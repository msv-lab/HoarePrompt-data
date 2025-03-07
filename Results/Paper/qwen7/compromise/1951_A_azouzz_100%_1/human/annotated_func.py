#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end represent valid directory names without leading zeros.
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
        
    #State: Output State: The output state will consist of a series of 'YES' or 'NO' responses based on the conditions evaluated for each string `s` read from input during the `t` iterations of the loop. For each iteration, if the count of '1's in the string `s` is greater than 2 and even, it prints 'YES'. If the count of '1's is greater than 2 but odd, it prints 'NO'. If the count of '1's is exactly 1, it also prints 'NO'. If the substring '11' exists in `s`, it prints 'NO'. Otherwise, it prints 'YES'.
#Overall this is what the function does:The function reads multiple strings `s` from input, each corresponding to a directory name. It checks each string for specific conditions related to the count of '1's and the presence of the substring '11'. Based on these conditions, it prints 'YES' or 'NO' for each string. Specifically, it prints 'YES' if the count of '1's is greater than 2 and even, or if the count of '1's is 0 or 2 and '11' is not present. Otherwise, it prints 'NO'. The function processes `t` such strings and outputs the results accordingly.

