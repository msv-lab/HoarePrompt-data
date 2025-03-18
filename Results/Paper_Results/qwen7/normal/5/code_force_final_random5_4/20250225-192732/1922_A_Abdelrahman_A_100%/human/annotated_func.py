#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings consisting of exactly n lowercase Latin letters.
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
        
    #State: All tests have been processed, `tests` is now 0, `i` is equal to the initial value of `tests`, `no` is either True or False depending on the final iteration's conditions, `slength` is the same as the initial input, `a` is the input string from the first iteration, `b` is the input string from the second iteration, `c` is the input string from the last iteration, and `counter` is equal to the length of the last input string `c` plus one.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer t (number of test cases), an integer n (length of strings), and three strings a, b, and c (each of length n). For each test case, it checks if the string c can be formed by concatenating substrings from strings a and b. If c can be formed, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function does not return any value.

