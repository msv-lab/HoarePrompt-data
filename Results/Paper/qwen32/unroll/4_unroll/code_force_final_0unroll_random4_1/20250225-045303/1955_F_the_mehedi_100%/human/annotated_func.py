#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains four integers p_i (0 ≤ p_i ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: a series of integers, each representing the computed `cnt` value for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates and prints a value based on these counts. The calculated value is determined by adding 1 if all counts of ones, twos, and threes are odd, and then adding half the value of each count (rounded down) to this sum.

