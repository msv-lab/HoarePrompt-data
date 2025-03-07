#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: i is 3, a is the first input integer, b is the second input integer, c is the third input integer, d is the fourth input integer, the values of a, b, c, and d are assigned the integer values from the input split by spaces, and the loop has executed 3 times.
#Overall this is what the function does:The function processes a series of test cases, each consisting of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates and prints a value based on these counts. Specifically, it computes the sum of half the counts of 1s, 2s, 3s, and 4s (using integer division), plus an additional 1 if the sum of the remainders when dividing the counts by 2 equals 3. The function executes this process for up to 10,000 test cases.

