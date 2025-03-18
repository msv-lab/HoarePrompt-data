#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9 for each pile. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State: t is an input integer, i is t-1, n is an input integer, l is a list of integers obtained from splitting the input string and converting each element to an integer, e is a set containing unique elements from the list l, m is the length of the list l.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t, an integer n, and a list of n integers representing the number of stones in each pile. For each test case, it checks if the number 1 exists in the list of stones. If 1 is found, it prints 'Bob'; otherwise, it prints 'Alice'. The function does not return any value but prints the result for each test case directly.

