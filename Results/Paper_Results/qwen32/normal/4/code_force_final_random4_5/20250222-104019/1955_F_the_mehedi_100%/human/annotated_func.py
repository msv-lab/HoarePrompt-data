#State of the program right berfore the function call: Each test case consists of four integers \( p_1, p_2, p_3, p_4 \) (0 \(\le\) \( p_i \) \(\le\) 200) representing the counts of ones, twos, threes, and fours in the sequence, respectively. The number of test cases \( t \) satisfies 1 \(\le\) \( t \) \(\le\) 10^4.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The accumulated value of `cnt` after `t` iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates a value based on these counts and prints the result. Specifically, it checks if the counts of ones, twos, and threes are all odd, and if so, increments a counter. It then adds half the value of each count (rounded down) to this counter. The function outputs the final counter value for each test case.

