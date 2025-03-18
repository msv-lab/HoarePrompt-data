#State of the program right berfore the function call: Each test case contains four integers p_i (0 ≤ p_i ≤ 200) representing the count of ones, twos, threes, and fours in the sequence, respectively. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: A sequence of integers printed for each test case, where each integer is the calculated `cnt` for that test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates and prints a value based on these counts.

