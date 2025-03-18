#State of the program right berfore the function call: Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of ones, twos, threes, and fours in the sequence. The number of test cases t satisfies 1 ≤ t ≤ 10^4.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: the final accumulated value of `cnt`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four non-negative integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates a value based on the counts and prints this value. The calculation involves checking if all counts of ones, twos, and threes are odd, and then adding half of each count (rounded down) to a cumulative total.

