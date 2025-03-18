#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: a list of t integers, each representing the final value of `cnt` for the respective test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours. For each test case, it calculates a value based on these counts and prints the result. Specifically, it checks if the counts of ones, twos, and threes are all odd and increments the result by one if true. Then, it adds half of each count (rounded down) to the result. The function outputs the calculated value for each test case.

