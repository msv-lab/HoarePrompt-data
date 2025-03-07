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
#Overall this is what the function does:The function `func_1` reads an integer `t`, then for each of the next `t` instances, it reads an integer `n` and a string `s`. It counts the number of '1's in the string `s` and prints 'YES' or 'NO' based on specific conditions related to the count of '1's and the presence of '11' in the string. The function does not return any value; it only prints output.

