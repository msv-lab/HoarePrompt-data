#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, representing the number of piles, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) represents the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is greater than 0, `tc` is `t-1`, `n` is an input integer, `a` is a sorted list of integers from the input, `maxsize` is the maximum value in the sorted list `a`, and `mexsize` is the smallest positive integer not present in the list `a`. If `mexsize` is greater than `maxsize`, then `mexsize` remains greater than `maxsize`. Otherwise, `mexsize` is less than or equal to `maxsize`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` representing the number of piles and a list of `n` integers representing the number of stones in each pile. It then determines the winner of a game between Alice and Bob based on the following rules: If the smallest positive integer not present in the list (MEX) is greater than the maximum number of stones in any pile, the winner is Alice if MEX is even, otherwise Bob. If the MEX is less than or equal to the maximum number of stones, the winner is Alice if MEX is odd, otherwise Bob. The function prints the winner for each test case. After processing all test cases, the function completes, leaving `t` greater than 0, `tc` equal to `t-1`, `n` as the last input integer, `a` as the last sorted list of integers, `maxsize` as the maximum value in the last list, and `mexsize` as the smallest positive integer not present in the last list.

