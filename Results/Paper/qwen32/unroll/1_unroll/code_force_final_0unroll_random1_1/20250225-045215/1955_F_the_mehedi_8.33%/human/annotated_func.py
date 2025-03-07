#State of the program right berfore the function call: Each test case consists of four integers \( p_1, p_2, p_3, p_4 \) (0 \(\le\) \( p_i \) \(\le\) 200), representing the number of ones, twos, threes, and fours in the sequence, respectively. There are \( t \) (1 \(\le\) \( t \) \(\le\) 10^4) such test cases.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: a list of integers, each representing the final value of `cnt` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of four integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates a value based on these counts and prints the result. The final state of the program is that it outputs the calculated value for each test case.

