#State of the program right berfore the function call: The function receives an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. For each test case, it receives an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) where a_i is the number of stones in the i-th pile. The sum of n over all test cases does not exceed 2·10^5.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: a sequence of `t` lines, each line being either 'Bob' or 'Alice', based on the presence of `1` in the corresponding list for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines and prints whether 'Bob' or 'Alice' wins based on whether the number `1` is present in the list of stones.

