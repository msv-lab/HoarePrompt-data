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
        
    #State: `start` and `end` are integers such that `start` <= `end`; `t` is 0; `n` is the integer value of the user input from the last iteration; `s` is the string value of the user input from the last iteration; `cnt1` is the number of occurrences of '1' in the last `s`.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the user, then for each of the next `t` iterations, it reads another integer `n` and a string `s`. It counts the number of '1's in `s` and prints 'YES' if the count is greater than 2 and even, or if there are no consecutive '1's in `s`. Otherwise, it prints 'NO'. The function does not accept `start` and `end` as parameters nor does it return any value.

