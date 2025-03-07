#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i (0 ≤ p_i ≤ 200) represents the count of numbers in the sequence that are 1, 2, 3, and 4 respectively, and the sum of p_i (i.e., p_1 + p_2 + p_3 + p_4) is equal to the initial length of the sequence.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: After all iterations of the loop, `a` is an empty list, and `cnt` is the total sum of `math.floor(x / 2)` for all elements `x` in `a` that were processed during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads counts of numbers 1, 2, 3, and 4. It then calculates the sum of the floor division of each number by 2 and prints this sum for each test case. The function does not return any value but prints the calculated sum for each test case.

