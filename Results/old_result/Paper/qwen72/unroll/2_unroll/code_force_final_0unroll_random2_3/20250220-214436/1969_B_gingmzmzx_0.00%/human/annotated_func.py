#State of the program right berfore the function call: The function definition is incomplete and does not provide the necessary parameters to solve the problem as described. The function should take a binary string `s` as an input parameter.
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
        
    #State: The loop will execute `n` times, and for each iteration, it will read a new binary string `s` from the input, convert it to a list of integers, and compute the value of `ans` based on the number of zeroes and ones in the list. The final value of `ans` for each iteration will be printed. The variables `s`, `zeroes`, `cnt`, and `ans` will be reset to their initial states at the beginning of each iteration.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, which represents the number of binary strings to process. For each of the `n` iterations, it reads a binary string `s` from the input, converts it to a list of integers, and calculates a value `ans` based on the counts of zeroes and ones in the list. The final value of `ans` for each binary string is printed. The function does not return any value; it only prints the results.

