#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, s is a binary string of length between 2 and 2 * 10^5, inclusive, consisting only of the characters '0' and '1'. The sum of the lengths of all strings s across all test cases does not exceed 2 * 10^5.
def func_1():
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        
        zeroes = s.count(0)
        
        cnt = [0, 0]
        
        ans = 0
        
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += zeroes - cnt[0]
        
        print(ans)
        
    #State: The output state consists of `t` integers, each representing the result of the corresponding test case after processing the binary string `s` according to the described logic.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a binary string. For each test case, it calculates and prints an integer value based on the specific logic applied to the binary string. The function does not accept any direct parameters but reads input from standard input. It outputs an integer for each test case, representing the result of the calculation performed on the corresponding binary string.

