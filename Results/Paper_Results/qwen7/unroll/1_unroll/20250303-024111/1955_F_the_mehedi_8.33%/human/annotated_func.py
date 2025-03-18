#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200), representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: The value of `cnt` after all iterations of the loop have finished, which is the sum of 1 for each instance where the counts of 1s, 2s, and 3s are equal and odd, plus the floor division of each count by 2.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates and prints the total count, which includes 1 for each instance where the counts of 1s, 2s, and 3s are equal and odd, plus half the count of each number rounded down.

