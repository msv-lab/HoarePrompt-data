#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After all iterations of the loop, `a` will be a sorted list of integers, `mexsize` will be the smallest positive integer not present in the list `a`, and `sz` will be the last element of the list `a`. `tc` will be `t - 1`, and `maxsize` will be the maximum value in the list `a`. If `mexsize` is greater than `maxsize`, it means that `mexsize` is the smallest missing positive integer larger than any number in the list. Otherwise, `mexsize` is the last value that was incremented during the loop, which is one more than the last element in the list `a` if all elements in `a` match their respective `mexsize` values during the loop iterations. The final output will be 'Alice' if `mexsize` is even, and 'Bob' if `mexsize` is odd.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) indicating the number of test cases, followed by \( t \) groups of data. Each group includes a positive integer \( n \) and a list of \( n \) integers. For each group, the function sorts the list of integers, finds the smallest positive integer not present in the list, and determines whether this integer is even or odd. Based on this determination, the function prints either "Alice" or "Bob". The function does not return any value but outputs the result for each test case.

