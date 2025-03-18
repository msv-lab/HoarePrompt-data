#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers where 0 <= p_i[j] <= 200 for j in [0, 1, 2, 3].
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: `_` is `t-1`, `a` is a list of integers derived from the input for the last test case, `cnt` is the sum of 1 (if the first three elements of `a` are all odd) and the floor division of each element in `a` by 2 for each of the `t` test cases.
#Overall this is what the function does:The function processes a series of test cases, where each test case is a list of four integers. For each test case, it calculates a count based on the following rules: it adds 1 to the count if the first three integers in the list are all odd, and then adds the floor division of each integer in the list by 2 to the count. The function prints the count for each test case and does not return any value. After the function concludes, the program state includes the printed counts for all test cases.

