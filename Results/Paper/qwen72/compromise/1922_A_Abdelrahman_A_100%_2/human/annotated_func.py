#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 20, and a, b, c are strings of length n consisting of lowercase Latin letters.
def func():
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: The values of `t`, `n`, `a`, `b`, and `c` remain unchanged. The loop has executed `tests` times, and for each iteration, either 'YES' or 'NO' has been printed based on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads multiple sets of inputs from the user, where each set includes an integer `slength` and three strings `a`, `b`, and `c` of length `slength`. For each set, it checks if the string `c` is different from both `a` and `b`, and if each character in `c` is either present in the corresponding position in `a` or `b`. If `c` meets these conditions, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value and does not modify the input variables `t`, `n`, `a`, `b`, or `c`. The loop runs `tests` times, where `tests` is an integer between 1 and 1000.

