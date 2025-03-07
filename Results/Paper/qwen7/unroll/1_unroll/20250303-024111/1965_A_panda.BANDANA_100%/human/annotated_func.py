#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each i, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: The output will depend on the input integers provided within the range of 1 to 10^4. For each input integer t, the program processes t lines of space-separated integers. It then checks the sorted unique list of these integers to determine if 'Alice' or 'Bob' should be printed based on specific conditions related to gaps between consecutive elements in the list.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer t indicating the number of subsequent test cases, followed by t lines of input. Each line contains a positive integer n and a list of n integers. The function sorts and removes duplicate integers from the list, then checks the gaps between consecutive integers. Based on the presence of gaps greater than one and their positions, the function determines and prints either 'Alice' or 'Bob'. The function does not return any value but prints the result for each test case.

