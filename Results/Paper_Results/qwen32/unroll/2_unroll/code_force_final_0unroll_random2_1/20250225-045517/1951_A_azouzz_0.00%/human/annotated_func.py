#State of the program right berfore the function call: start and end are integers such that start <= end.
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
        
    #State: start and end are integers such that start <= end; t is an input integer.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads another integer `n` and a string `s`. It then checks the number of '1's in the string `s` and prints 'YES' or 'NO' based on specific conditions: 'YES' if there are more than 2 '1's and the count is even, or if there is at most one '1'; 'NO' if there are more than 2 '1's and the count is odd, or if there are two consecutive '1's in the string.

