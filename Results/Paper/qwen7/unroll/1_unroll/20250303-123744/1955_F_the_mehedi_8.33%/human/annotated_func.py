#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, p_i is a list of four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence, respectively, such that the sum of p_i is at least 1.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: Output State: The value of `cnt` is calculated based on the input lists `a`. For each test case, `cnt` is incremented by 1 if the first three elements of the list `a` are equal and odd, and then `cnt` is further incremented by half the value of each element in the list, rounded down. The final value of `cnt` for each test case is printed.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it calculates a value `cnt` based on the input list `a` containing four non-negative integers representing the counts of 1s, 2s, 3s, and 4s in the initial sequence. It increments `cnt` by 1 if the first three elements of the list `a` are equal and odd, and then increments `cnt` by half the value of each element in the list, rounded down. Finally, it prints the calculated value of `cnt` for each test case.

