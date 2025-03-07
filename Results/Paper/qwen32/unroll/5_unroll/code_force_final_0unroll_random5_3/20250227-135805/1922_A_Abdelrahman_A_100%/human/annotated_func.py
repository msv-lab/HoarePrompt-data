#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 20, and a, b, and c are strings each consisting of exactly n lowercase Latin letters.
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
        
    #State: The variables `i`, `slength`, `a`, `b`, `c`, `no`, `counter`, and `x` are in an undefined state as they are local to each iteration of the loop. The only persistent outputs are the series of 'YES' or 'NO' printed for each test case.
#Overall this is what the function does:The function processes a series of test cases, where each test case includes three strings `a`, `b`, and `c` of equal length. For each test case, it determines if string `c` can be formed by selecting characters from the corresponding positions in strings `a` and `b`. It prints 'YES' if `c` can be formed in this manner, otherwise it prints 'NO'.

