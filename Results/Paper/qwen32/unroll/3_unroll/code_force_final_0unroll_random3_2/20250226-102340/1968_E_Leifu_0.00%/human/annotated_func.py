#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each test case, n is an integer such that 2 <= n <= 10^3.
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
        
    #State: The printed output for each test case, which includes the pairs '1 1', '1 2', and additional pairs based on the value of `n` as described above.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, and for each test case, it reads an integer `n`. It then prints specific pairs of numbers: '1 1', '1 2', and additional pairs based on the value of `n`. If `n` is 3, it prints '2 3'. Otherwise, it prints '2 4' followed by pairs of the form 'j j' for each `j` from 4 to `n`.

