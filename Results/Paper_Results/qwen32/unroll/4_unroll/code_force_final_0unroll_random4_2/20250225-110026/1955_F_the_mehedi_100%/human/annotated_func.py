#State of the program right berfore the function call: Each test case is represented by four non-negative integers \( p_1, p_2, p_3, p_4 \) (where \( 0 \le p_i \le 200 \)) indicating the counts of ones, twos, threes, and fours in the sequence. The function receives multiple test cases, with the first line containing an integer \( t \) (where \( 1 \le t \le 10^4 \)) representing the number of test cases.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: result1 result2 ... resultt
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four non-negative integers representing the counts of ones, twos, threes, and fours in a sequence. For each test case, it calculates a result based on these counts and prints the result. The final state of the program is the output of results for all test cases.

