#State of the program right berfore the function call: start and end are integers such that start <= end.
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
        
    #State: start and end are integers such that start <= end; t is an input integer.
#Overall this is what the function does:The function reads an integer `t` from the input, then for each of the next `t` lines, it reads an integer `n` and a string `s`. It counts the number of '1's in the string `s` and prints 'YES' if the count is greater than 2 and even, or if the count is exactly 0 or 1 and there are no consecutive '1's. Otherwise, it prints 'NO'.

