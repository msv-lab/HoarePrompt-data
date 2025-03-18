#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: After all iterations of the loop, `t` must be greater than 2, `i` will be equal to `t-1`, and `j` will be equal to the final value of `n` for the last iteration. If `n` is exactly 3 during the last iteration, then `j` will be 3. Otherwise, `j` will be equal to the final value of `n` which is at least 4.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (1 ≤ t ≤ 50) and an integer `n` (2 ≤ n ≤ 10^3). For each test case, it prints a sequence of pairs of integers. Specifically, it always prints '1 1' and '1 2'. Depending on the value of `n`, it may print additional pairs, including '2 3' if `n` is 3, and pairs 'j j' for `j` ranging from 4 to `n`. After processing all test cases, the function does not return any value.

