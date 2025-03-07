#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a (length n) represents the initial number of stones in each pile, where 1 ≤ a_i ≤ 10^9 for all i. It is also given that the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Postcondition: `tc` is equal to `t-1`, `t` is an input integer, `n` is the last input integer for the final test case, `a` is a sorted list of integers representing the initial number of stones in each pile for the final test case, `maxsize` is the maximum value in the list `a`, and `mexsize` is the smallest positive integer not present in the list `a`. The value of `mexsize` is either greater than `maxsize` or is the smallest integer greater than `maxsize` if there are gaps in the sequence of integers in `a`. If `mexsize` is greater than `maxsize`, the function prints 'Alice' if `mexsize` is even, otherwise 'Bob'. If `mexsize` is less than or equal to `maxsize`, the function prints 'Alice' if `mexsize` is odd, otherwise 'Bob'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (number of piles), and a list of n integers a representing the initial number of stones in each pile. For each test case, it determines whether 'Alice' or 'Bob' wins based on the distribution of stones. Specifically, it calculates the maximum value (`maxsize`) and the smallest missing positive integer (`mexsize`) in the list `a`. If `mexsize` is greater than `maxsize`, it prints 'Alice' if `mexsize` is even, otherwise 'Bob'. If `mexsize` is less than or equal to `maxsize`, it prints 'Alice' if `mexsize` is odd, otherwise 'Bob'.

