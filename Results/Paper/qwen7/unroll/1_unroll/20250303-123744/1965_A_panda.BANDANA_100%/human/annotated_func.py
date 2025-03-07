#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9; the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will consist of a series of lines, each corresponding to the result of one iteration of the loop. For each iteration, if the sorted unique elements of the list `l` either do not contain 1 or contain only one unique element, the output will be 'Alice'. Otherwise, it will check the difference between consecutive elements in the sorted unique list. If any difference is greater than 1, it will print 'Bob' if the index of the difference is odd, and 'Alice' if the index is even, breaking out of the loop. If no such difference is found, it will print 'Alice' if the length of the sorted unique list is odd, and 'Bob' if the length is even.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t indicating the number of test cases, an integer n representing the number of piles, and a list of n integers representing the number of stones in each pile. For each test case, it checks the sorted unique elements of the stone counts. If the list contains 1 or only one unique element, it outputs 'Alice'. Otherwise, it examines the differences between consecutive elements in the sorted unique list. If any difference is greater than 1, it prints 'Bob' if the index of the difference is odd, and 'Alice' if the index is even. If no such difference is found, it prints 'Alice' if the length of the sorted unique list is odd, and 'Bob' if the length is even.

