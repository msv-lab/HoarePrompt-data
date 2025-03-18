#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i (0 ≤ p_i ≤ 200) represents the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: After the loop executes all the iterations, `a` is an empty list, `cnt` is the sum of the floor divisions of all elements in the original list `a` by 2, and `t` is a positive integer such that \(1 \leq t \leq 10^4\).
    #
    #In this final state, the list `a` has been fully processed, and `cnt` contains the total sum of the floor division of each element in `a` by 2 across all iterations of the loop.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of four integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates the sum of the floor division of each count by 2 and prints the result. After processing all test cases, it outputs the total count for each test case.

