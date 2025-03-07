#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: All test cases have been processed, and for each test case, the program has determined whether Alice or Bob wins based on the smallest missing positive integer (MEX) in the sorted list of integers `a` and compared it with the maximum value in the list `a`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers. For each test case, it determines the smallest missing positive integer (MEX) in the list and compares it with the maximum value in the list. Based on this comparison, it prints 'Alice' if the MEX is even and greater than the maximum value, or if the MEX is odd and less than or equal to the maximum value; otherwise, it prints 'Bob'.

