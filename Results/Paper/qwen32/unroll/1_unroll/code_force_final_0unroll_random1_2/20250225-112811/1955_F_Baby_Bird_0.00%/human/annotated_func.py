#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains four integers p_i (0 ≤ p_i ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence, respectively.
def func():
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: the results of `sum(p) // 2` for each test case, concatenated and separated by spaces.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a result based on these counts and prints the result. The result for each test case is determined by checking if exactly three of the first three counts are odd, adding 1 if true, and then adding half the sum of all four counts.

