#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The output state is determined by the results of each test case. For each test case, the program prints either 'Alice' or 'Bob' based on the conditions specified in the loop. The variable `t` remains unchanged as it represents the number of test cases. The variables `n`, `l`, `lis`, and `test` are local to each iteration and do not persist after the loop completes.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines and prints the winner ('Alice' or 'Bob') based on specific conditions related to the sorted unique number of stones in the piles.

