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
        
    #State: The output state consists of `t` lines of either 'YES' or 'NO' based on the conditions evaluated for each input string `s`. The variables `start` and `end` remain unchanged.
#Overall this is what the function does:The function `func_1` reads an integer `t` from the input, followed by `t` pairs of an integer `n` and a string `s`. For each string `s`, it prints 'YES' if the count of '1's in `s` is greater than 2 and even, or if `s` does not contain '11'. Otherwise, it prints 'NO'. The function does not return any value and the variables `start` and `end` mentioned in the annotations are not used or relevant to the function's behavior.

