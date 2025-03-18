#State of the program right berfore the function call: start and end are integers such that start <= end, and both represent valid directory names without leading or trailing spaces.
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
        
    #State: Output State: The output state will consist of a series of "YES" and "NO" based on the conditions evaluated for each string `s` provided in the loop. For each iteration, if the count of '1's in the string `s` is greater than 2 and even, it prints "YES". If the count of '1's is greater than 2 but odd, or if there are consecutive '1's ('11'), it prints "NO". If the count of '1's is exactly 1, it also prints "NO". Otherwise, it prints "YES".
#Overall this is what the function does:The function processes multiple strings `s` (each representing a directory name) and prints "YES" or "NO" based on specific conditions related to the count of '1's in each string. For each string, if the count of '1's is greater than 2 and even, it prints "YES". If the count of '1's is greater than 2 but odd, or if there are consecutive '1's ('11'), it prints "NO". If the count of '1's is exactly 1, it also prints "NO". Otherwise, it prints "YES". The function does not accept any parameters and does not return any value.

