#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a (length n) represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: All elements from the list `a` have been processed, and the loop has completed all its iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) representing the number of test cases, followed by a positive integer \( n \) and a list of \( n \) integers \( a \) representing the number of stones in each of \( n \) piles. For each test case, it determines whether Alice or Bob wins based on the maximum element in the sorted list \( a \) and the smallest missing positive integer (Mex) in the list. If the Mex is greater than the maximum element in the list, it prints "Alice" if Mex is even, otherwise "Bob". If the Mex is less than or equal to the maximum element, it prints "Alice" if Mex is odd, otherwise "Bob".

