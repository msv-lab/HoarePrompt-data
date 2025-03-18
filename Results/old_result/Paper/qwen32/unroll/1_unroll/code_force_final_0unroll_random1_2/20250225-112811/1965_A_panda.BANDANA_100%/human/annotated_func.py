#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a list a of n integers where each a_i is such that 1 <= a_i <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: The output state consists of `t` lines of either 'Alice' or 'Bob', determined by the conditions specified in the loop for each test case. The variables `t`, `n`, `l`, `lis`, and `test` do not retain their values after the loop completes as they are reinitialized in each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then determines and prints either 'Alice' or 'Bob' based on specific conditions related to the sorted unique elements of the list.

