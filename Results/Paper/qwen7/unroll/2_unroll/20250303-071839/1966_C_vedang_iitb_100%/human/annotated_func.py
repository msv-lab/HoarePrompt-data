#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a_1, a_2, ..., a_n represents the initial number of stones in each of the n piles, where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will consist of multiple lines, each line containing either "Alice" or "Bob". For each test case (tc) provided in the input, the program determines whether "Alice" or "Bob" wins based on the conditions specified in the loop. Specifically, it checks if the smallest missing positive integer (`mexsize`) is greater than the maximum value in the list (`maxsize`). If `mexsize` is greater, it prints "Alice" if `mexsize` is even, and "Bob" if `mexsize` is odd. If `mexsize` is not greater, it prints "Alice" if `mexsize` is odd, and "Bob" if `mexsize` is even.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t representing the number of test cases, followed by an integer n and a list of n integers a. It calculates the smallest missing positive integer (`mexsize`) and compares it with the maximum value in the list (`maxsize`). Based on the comparison and the parity of `mexsize`, it outputs "Alice" or "Bob" for each test case.

