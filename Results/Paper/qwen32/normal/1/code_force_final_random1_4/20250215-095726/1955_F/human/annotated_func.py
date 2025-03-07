#State of the program right berfore the function call: Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The output state is a sequence of integers, each representing the result of the computation for each test case, printed one per line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it computes a result based on these counts and prints the result. The result is determined by checking if exactly three out of the first three counts (ones, twos, threes) are odd, and then adding half the sum of all four counts.

