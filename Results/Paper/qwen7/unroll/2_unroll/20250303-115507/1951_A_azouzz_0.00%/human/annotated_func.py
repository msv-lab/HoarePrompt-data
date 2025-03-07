#State of the program right berfore the function call: start and end are integers such that start <= end, and both start and end are used to filter folder names which should be digits within the specified range.
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
        
    #State: Output State: The output state will consist of a series of 'YES' and 'NO' based on the conditions evaluated for each iteration of the loop. For each input 'n' and string 's', if the count of '1's is greater than 2 and even, it prints 'YES'. If the count of '1's is greater than 2 and odd, or equal to 1, it prints 'NO'. If '11' is found in the string 's', it prints 'NO'. Otherwise, it prints 'YES'.
#Overall this is what the function does:The function reads multiple test cases, where each case consists of an integer `n` followed by a string `s`. It then evaluates the string `s` based on specific conditions related to the count of '1's in the string and the presence of '11'. Depending on these evaluations, it prints either 'YES' or 'NO' for each test case.

