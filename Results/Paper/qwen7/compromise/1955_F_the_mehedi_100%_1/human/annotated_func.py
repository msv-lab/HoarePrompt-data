#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively, such that 0 ≤ p_i[0] + p_i[1] + p_i[2] + p_i[3] ≤ 200.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: After the loop executes all iterations, `cnt` is the sum of the floor division of each element in `a` by 2, repeated for the number of times specified by the input.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a list of four integers representing counts of 1s, 2s, 3s, and 4s. It calculates a count based on specific conditions involving these integers and prints the result. Specifically, it increments a counter by 1 if certain conditions are met and then adds the floor division of each integer in the list by 2 to the counter. The function does not return any value but prints the final count for each test case.

