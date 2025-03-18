#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: A series of sums, each on a new line, corresponding to the sum of elements at even indices of the sorted list for each iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes an integer `n` and a list of `2n` integers. It sorts the list and then calculates and prints the sum of the elements at even indices of the sorted list.

