#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers (0 <= p_i <= 200) representing the number of ones, twos, threes, and fours in the sequence.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: _ is t-1, t is an integer such that 1 <= t <= 10^4, a is a list of integers input by the user, cnt is the sum of 1 (if the first three elements of `a` are all odd) and the floor division of each element in `a` by 2, repeated for each of the `t` test cases.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case is defined by a list of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a value `cnt` which is the sum of 1 (if the first three elements of the list are all odd) and the floor division of each element in the list by 2. The function then prints this value for each test case. After processing all test cases, the function does not return any value.

