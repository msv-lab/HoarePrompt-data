#State of the program right berfore the function call: Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: `cnt` is `n * (1 + sum(math.floor(x / 2) for x in a))` if the first three elements of `a` are all odd, otherwise `cnt` is `n * sum(math.floor(x / 2) for x in a)`. The list `a` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a value based on these counts and prints the result. Specifically, it checks if the first three counts are odd; if so, it adds one to the count. Then, it adds half of each count (rounded down) to this value. The function outputs this calculated value for each test case.

