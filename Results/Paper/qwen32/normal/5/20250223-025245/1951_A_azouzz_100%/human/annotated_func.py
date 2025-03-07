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
        
    #State: `start` and `end` are integers such that `start` <= `end`; `t` is 0; `n` is the last input integer; `s` is the last value of the user input; `cnt1` is the number of occurrences of '1' in the last `s`. Regardless of the value of `cnt1`, it does not affect the output state since `t` is now 0 and the loop has finished executing.
#Overall this is what the function does:The function reads an integer `t` from the user, then for each of the next `t` iterations, it reads another integer `n` and a string `s`. It counts the number of '1's in `s` and prints 'YES' if the count is even and greater than 2, or if there is at most one '1' and no '11' substring in `s`. Otherwise, it prints 'NO'. The function does not return any value explicitly.

