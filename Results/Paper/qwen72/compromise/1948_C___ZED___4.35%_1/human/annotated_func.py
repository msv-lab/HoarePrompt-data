#State of the program right berfore the function call: The function should take three parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and for each test case, an integer n (2 ≤ n ≤ 2·10^5) where n is even, and two strings of length n containing only the characters '<' and '>' representing the arrows in the first and second rows of the grid, respectively. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for i in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        if b[-2] != '>':
            print('NO')
        elif n == 1:
            print('YES')
        else:
            no_path = True
            for k in range(0, n, 2):
                if b[k] != '>':
                    no_path = False
            if not no_path:
                no_path = True
                for k in range(1, n - 1, 2):
                    print(k)
                    if a[k] != '>':
                        no_path = False
            if no_path:
                print('YES')
            else:
                print('NO')
        
    #State: `i` is `t-1`, `n` is the last input integer, `a` is the last input string, `b` is the last input string, and `no_path` is the final boolean value determined by the conditions in the loop.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads an integer `n` and two strings `a` and `b` of length `n` containing only the characters '<' and '>'. The function then determines whether it is possible to make all characters in both strings point in the same direction by swapping characters within each string. It prints 'YES' if it is possible and 'NO' otherwise. After processing all test cases, the function concludes, and the final state includes the last processed values of `i`, `n`, `a`, `b`, and `no_path`.

