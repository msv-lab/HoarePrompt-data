#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i (0 ≤ p_i ≤ 200) represents the count of numbers of types 1, 2, 3, and 4 in the initial sequence respectively, where i ∈ {0, 1, 2, 3}.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i (0 ≤ p_i ≤ 200) represents the count of numbers of types 1, 2, 3, and 4 in the final sequence respectively, where i ∈ {0, 1, 2, 3}.
    #
    #Explanation: After executing the loop for each test case, the value of `cnt` is calculated based on the conditions given in the loop. The final value of `cnt` is printed, which represents the sum of the original numbers divided by 2 and a special condition check. The counts of numbers of types 1, 2, 3, and 4 in the final sequence are not directly affected by the loop and remain as the initial counts provided in the input.
#Overall this is what the function does:The function processes a series of test cases, each defined by counts of four types (1, 2, 3, and 4) of numbers within the range of 0 to 200. For each test case, it calculates a value `cnt` based on specific conditions involving the input counts and prints this value. The function does not return any value but outputs the calculated `cnt` for each test case.

