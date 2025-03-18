#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and for each of the t test cases, n is an integer such that 2 <= n <= 10^3.
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
        
    #State: The output will be a series of printed lines for each test case. For each test case, the output will start with '1 1' and '1 2'. If `n` is 3, it will be followed by '2 3'. Otherwise, it will be followed by '2 4' and then 'j j' for each `j` from 4 to `n`.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` where 2 <= n <= 10^3. For each test case, it prints a specific sequence of pairs of integers. The sequence starts with '1 1' and '1 2'. If `n` is 3, it continues with '2 3'. Otherwise, it continues with '2 4' followed by 'j j' for each integer `j` from 4 to `n`.

