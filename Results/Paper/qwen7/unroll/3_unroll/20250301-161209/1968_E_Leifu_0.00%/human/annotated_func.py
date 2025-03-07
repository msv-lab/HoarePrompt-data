#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: Output State: t lines, each line contains:
    #- '1 1'
    #- '1 2'
    #- If the input n equals 3, then the line contains: '2 3'
    #- Otherwise, the line contains: '2 4'
    #- For j from 4 to n (inclusive), the line contains: j space j
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t`. For each test case, it reads an integer `n` and prints a sequence of strings. Specifically, it always prints "1 1" and "1 2". If `n` equals 3, it prints "2 3"; otherwise, it prints "2 4" followed by a sequence of strings where each string contains an integer `j` from 4 to `n`, paired with itself. After processing all `t` test cases, the function does not return any value.

