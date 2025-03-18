#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: Output State: The output state is a series of integers representing the result of the loop for each test case. For each test case, the output is calculated as follows: 
    #1. Read a line of input and split it into four integers, which represent the counts of 1s, 2s, 3s, and 4s in the initial sequence.
    #2. For each integer in the first three positions (counts of 1s, 2s, and 3s), if it is odd, it contributes 1 to a counter; otherwise, it contributes 0. If all three of these counters sum to 3, then add 1 to another counter; otherwise, do nothing.
    #3. Add half of the sum of the four integers (integer division) to the previous counter.
    #4. Print the final value of the counter for each test case.
    #
    #In summary, the output state is a list of integers where each integer represents the computed value for each respective test case based on the rules described above.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates a value based on specific conditions and prints the result. Specifically, it checks if the counts of 1s, 2s, and 3s are all odd, and if so, adds 1 to a counter. It also adds half of the total count of all numbers (integer division) to this counter. The final value of the counter for each test case is printed.

