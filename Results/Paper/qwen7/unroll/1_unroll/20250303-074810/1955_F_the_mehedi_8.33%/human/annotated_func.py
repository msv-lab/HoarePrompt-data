#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, there are four non-negative integers p_i (0 ≤ p_i ≤ 200) representing the counts of 1s, 2s, 3s, and 4s in the initial sequence.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: The value of `cnt` is calculated based on the given conditions for each test case. Specifically, `cnt` is incremented by 1 if the first three elements of the input list `a` are equal and odd, and then `cnt` is further incremented by half the value of each element in the list, rounded down. The final value of `cnt` for each test case is printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in an initial sequence. For each test case, it calculates a value `cnt` based on specific conditions: incrementing `cnt` by 1 if the first three elements are equal and odd, and then adding half the value of each element in the list, rounded down. Finally, it prints the calculated value `cnt` for each test case.

