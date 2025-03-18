#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: The value of `cnt` after all iterations of the loop have finished, which is the sum of 1 for each condition where `a[0] % 2`, `a[1] % 2`, and `a[2] % 2` are all 1, plus the floor division of each element in `a` by 2.
    #
    #This means for each test case, `cnt` will be incremented by 1 for each set of counts (p_i, q_i, r_i) where the counts of 1s, 2s, and 3s are all odd, and then incremented by the half of each count in the list `a`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s. For each test case, it increments a counter by 1 if the counts of 1s, 2s, and 3s are all odd, and then adds half of each count to the counter. Finally, it prints the computed counter value for each test case.

