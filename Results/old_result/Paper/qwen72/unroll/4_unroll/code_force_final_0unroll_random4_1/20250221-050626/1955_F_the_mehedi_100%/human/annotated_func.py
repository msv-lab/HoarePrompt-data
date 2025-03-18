#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i are integers such that 0 <= p_i <= 200, representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: For each test case, the output is the value of `cnt` after the loop has finished executing. `cnt` is calculated by adding 1 if all the first three elements of the list `a` are odd, and then adding the integer division of each element in `a` by 2. The initial state of `t` and `p_i` remains unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case involves a list of four integers representing counts of ones, twos, threes, and fours. For each test case, it calculates a value `cnt` which is incremented by 1 if the first three integers in the list are all odd, and then by the integer division of each integer in the list by 2. The function prints the value of `cnt` for each test case. The initial state of the input variables `t` and `p_i` remains unchanged, and the function does not return any value.

