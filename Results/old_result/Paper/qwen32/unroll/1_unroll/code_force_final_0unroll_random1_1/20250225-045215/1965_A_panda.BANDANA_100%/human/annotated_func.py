#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of two lines: the first line contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: a sequence of "Alice" or "Bob" strings, one for each test case.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines the winner of a game between Alice and Bob based on the sorted unique number of stones in the piles and prints the winner's name ("Alice" or "Bob").

