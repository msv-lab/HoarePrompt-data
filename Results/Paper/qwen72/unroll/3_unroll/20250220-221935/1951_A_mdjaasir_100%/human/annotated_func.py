#State of the program right berfore the function call: start and end are integers where 0 <= start <= end.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: `start` and `end` remain unchanged, and `t` remains the same. The values of `n`, `a`, and `count` are undefined after the loop, as they depend on the last input provided.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads another integer `n` and a string `a` from the user input. The function then checks the string `a` for the number of occurrences of the character '1'. If the count of '1's is 0, greater than 2 and even, or exactly 2 with the two '1's not adjacent, it prints 'YES'. Otherwise, it prints 'NO'. The function does not modify any external variables or state.

