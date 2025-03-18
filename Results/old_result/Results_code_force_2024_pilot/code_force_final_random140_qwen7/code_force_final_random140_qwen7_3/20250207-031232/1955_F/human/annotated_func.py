#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a quadruple of non-negative integers (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, i equals t, and a, b, c, and d are integers obtained from the input split by spaces for the last iteration.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates and prints the total count of even numbers (1s and 2s divided by 2) plus a special condition based on the remainders when dividing the counts of 1s, 2s, and 3s by their respective values. The function does not return any value but prints the result for each test case.

