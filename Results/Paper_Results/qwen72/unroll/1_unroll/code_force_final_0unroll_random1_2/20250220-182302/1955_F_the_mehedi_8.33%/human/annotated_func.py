#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each of the four integers p_i in the sequence is an integer such that 0 <= p_i <= 200.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The value of `t` remains unchanged, and for each iteration, the variable `cnt` is calculated based on the input sequence `a`. After all iterations, the final output for each sequence `a` is the sum of 1 (if the first three integers in `a` are equal and odd) and the floor division of each integer in `a` by 2. The values of `p_i` in the sequence `a` are not retained after each iteration.
#Overall this is what the function does:The function `func` processes a series of input sequences, each containing four integers `p_i` (where 0 <= p_i <= 200), for a total of `t` iterations (where 1 <= t <= 10^4). For each sequence, it calculates a value `cnt` which is the sum of 1 (if the first three integers in the sequence are equal and odd) and the floor division of each integer in the sequence by 2. The function then prints this calculated value for each sequence. The value of `t` remains unchanged, and the values of `p_i` in each sequence are not retained after processing.

