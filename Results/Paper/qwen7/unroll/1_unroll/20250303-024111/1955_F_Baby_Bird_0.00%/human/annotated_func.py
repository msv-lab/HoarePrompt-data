#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, there are four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: Output State: The output state is a series of integers resulting from the evaluation of the given loop for each test case. For each test case, the output is calculated based on the following logic:
    #
    #1. Read four integers \( p_i \) (representing counts of 1s, 2s, 3s, and 4s).
    #2. Transform each \( p_i \) to its nearest even number.
    #3. Check if the first three transformed numbers (1s, 2s, 3s) are all odd.
    #4. If the condition in step 3 is true, add 1 to the result; otherwise, add 0.
    #5. Add half of the sum of all transformed numbers (integer division).
    #
    #The final output state is a list of these results for each test case.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s. For each test case, it transforms each count to the nearest even number, checks if the first three transformed counts are all odd, and adds 1 to the result if true, otherwise adds 0. It then adds half of the sum of all transformed counts (using integer division). The function outputs a list of these results for each test case.

