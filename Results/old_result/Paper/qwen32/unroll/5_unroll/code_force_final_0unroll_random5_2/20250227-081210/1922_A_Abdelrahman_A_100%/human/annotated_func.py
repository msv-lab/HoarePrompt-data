#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, for each test case n is an integer such that 1 <= n <= 20, and a, b, c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: `tests` is unchanged; `t` is unchanged; `a`, `b`, `c`, and `n` have the values from the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three strings of equal length. For each test case, it checks if the third string can be formed by selecting characters from the corresponding positions in the first two strings. If it can, it outputs 'YES'; otherwise, it outputs 'NO'.

