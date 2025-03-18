#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, there are four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: The value of `cnt` is calculated based on the given conditions for each test case. Specifically, `cnt` is incremented by 1 if the counts of 1s, 2s, and 3s in the input list are all odd, and then `cnt` is further incremented by half the sum of all elements in the list, rounded down. The final value of `cnt` for each test case is printed.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s. It calculates a total count based on specific conditions: incrementing by 1 if the counts of 1s, 2s, and 3s are all odd, and then adding half the sum of all elements in the list, rounded down. Finally, it prints the calculated total count for each test case.

