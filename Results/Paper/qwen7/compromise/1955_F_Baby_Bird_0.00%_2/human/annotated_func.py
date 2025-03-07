#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, there are four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: Output State: The output state consists of a series of integers, each representing the result of the print statement for each test case. For each test case, the result is either 0 or 1 plus the sum of the elements in the list `p` divided by 2. The value 0 or 1 is determined by whether the first three elements of the list `p` (representing counts of 1s, 2s, and 3s) are all odd, and then adding the integer division of the sum of all elements in `p` by 2.
    #
    #For example, if the input for a test case is "3" followed by "1 2 3 4", the list `p` would be [1, 2, 3, 4]. The expression `(sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3)` evaluates to 0 because not all of the first three elements are odd. Then, `sum(p) // 2` is `10 // 2`, which is 5. So the output for this test case would be `5`.
    #
    #Output State: A series of integers where each integer is either 0 or 1 plus the sum of the elements in the list `p` divided by 2 for each test case.
#Overall this is what the function does:The function processes a series of test cases, where each test case is defined by four non-negative integers representing the counts of 1s, 2s, 3s, and 4s. For each test case, it checks if the counts of 1s, 2s, and 3s are all odd. If they are, it sets the result to 1; otherwise, it sets the result to 0. Then, it adds half the sum of all counts (rounded down) to this result. The function outputs a series of integers, one for each test case, representing the computed results.

