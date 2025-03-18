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
        
    #State: The value of `t` remains unchanged, and the sequence of integers `p_i` (where 1 <= i <= 4) remains unchanged. For each iteration, the loop prints the value of `cnt`, which is calculated as the sum of 1 (if the first three elements of the list `a` are equal and odd) and the floor division of each element in `a` by 2.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 10^4`. For each of the `t` test cases, it reads a sequence of four integers `p_i` (where `0 <= p_i <= 200`) from the input, calculates a value `cnt` based on the sequence, and prints `cnt`. The value `cnt` is the sum of 1 (if the first three elements of the sequence are equal and odd) and the floor division of each element in the sequence by 2. The function does not modify the input values `t` or `p_i`.

