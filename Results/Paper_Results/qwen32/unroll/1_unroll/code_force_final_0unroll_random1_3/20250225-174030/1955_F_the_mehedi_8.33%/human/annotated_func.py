#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each test case consists of four integers p_i (0 ≤ p_i ≤ 200) representing the number of ones, twos, threes, and fours in the sequence, respectively.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] == a[1] == a[2] and a[0] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The output state consists of `t` lines, each line containing the result of the processing for one test case, which is the value of `cnt` after processing the counts of ones, twos, threes, and fours for that test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of four integers representing the counts of ones, twos, threes, and fours. For each test case, it calculates a value based on these counts and prints the result. The calculation involves checking if the counts of ones, twos, and threes are equal and odd, and then summing half the counts of each number (rounded down). The output is one line per test case containing the calculated value.

