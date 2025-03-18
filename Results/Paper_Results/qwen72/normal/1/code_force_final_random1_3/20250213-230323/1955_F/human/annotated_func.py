#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, p_i are integers such that 0 ≤ p_i ≤ 200, representing the counts of the integers 1, 2, 3, and 4 in the sequence.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `p` is a list of the nearest even numbers derived from the input integers, the loop has run `t` times, and there are 0 iterations left.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, it reads a list of integers `p` (0 ≤ p_i ≤ 200) representing counts of the integers 1, 2, 3, and 4 in a sequence. It then processes these counts to determine and print a value for each test case. The value printed is the sum of two components: 1) 1 if the first three elements of `p` (after being adjusted to the nearest even number) have an odd sum, and 0 otherwise; 2) half the sum of the adjusted `p` values. After processing all test cases, the function completes without returning any value.

