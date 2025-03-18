#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a list of integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
def func():
    tc = int(input())
    while tc > 0:
        n = int(input())
        
        arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [
            0]
        
        dp = True
        
        n = len(arr) - 1
        
        for i in range(1, n):
            dp = arr[i] - arr[i + 1] > 1 or not dp
        
        print('Alice' if dp else 'Bob')
        
        tc -= 1
        
    #State: tc is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers. For each test case, it determines whether 'Alice' or 'Bob' wins based on the differences between the sorted unique integers in the list. The function outputs 'Alice' if any two consecutive integers in the sorted list have a difference greater than 1, otherwise it outputs 'Bob'.

