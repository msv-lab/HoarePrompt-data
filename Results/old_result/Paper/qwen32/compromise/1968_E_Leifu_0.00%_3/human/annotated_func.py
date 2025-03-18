#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 50) representing the number of test cases. Each of the following t lines contains a single integer n (2 ≤ n ≤ 10^3) representing the size of the n x n grid for each test case.
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
        
    #State: `t` is an integer representing the number of test cases, where 1 ≤ t ≤ 50; the loop has executed `t` times; for each test case, the program prints "1 1", "1 2", and if `n` is 3, it prints "2 3", otherwise it prints "2 4" followed by lines from "4 4" to "n n" where each line contains the same number printed twice, separated by a space. The values of `t` and `n` remain unchanged after all iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the size of an n x n grid. It then prints specific pairs of numbers based on the value of `n`. For each test case, it prints "1 1", "1 2", and either "2 3" if `n` is 3, or "2 4" followed by pairs "j j" for `j` ranging from 4 to `n`.

