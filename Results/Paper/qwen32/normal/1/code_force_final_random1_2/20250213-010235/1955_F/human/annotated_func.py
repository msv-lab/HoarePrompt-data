#State of the program right berfore the function call: Each test case consists of four non-negative integers \( p_1, p_2, p_3, p_4 \) (where \( 0 \leq p_i \leq 200 \)) representing the counts of ones, twos, threes, and fours in the sequence, respectively. The total number of test cases \( t \) satisfies \( 1 \leq t \leq 10^4 \).
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: Each element in `p` is the nearest even integer less than or equal to its original value, and the printed output for each iteration is the sum of these even numbers divided by 2.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four non-negative integers representing counts of ones, twos, threes, and fours. For each test case, it calculates and prints a result based on these counts. Specifically, it checks if exactly three of the first three counts are odd and adds this boolean condition (1 for true, 0 for false) to half the sum of all four counts rounded down to the nearest even number.

