#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5; the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state consists of the names "Alice" or "Bob" printed for each test case based on the conditions inside the loop. For each test case, if `mexsize` (the smallest non-negative integer not present in the sorted list `a`) is greater than `maxsize` (the maximum value in the list `a`), then "Alice" is printed if `mexsize` is even, and "Bob" is printed if `mexsize` is odd. Otherwise, "Alice" is printed if `mexsize` is odd, and "Bob" is printed if `mexsize` is even.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer t indicating the number of test cases, followed by a positive integer n and a list of n integers representing the number of stones in each pile. For each test case, it calculates the smallest non-negative integer not present in the sorted list of stones (`mexsize`) and compares it with the maximum value in the list (`maxsize`). Based on the comparison and the parity of `mexsize`, it prints either "Alice" or "Bob" for each test case.

