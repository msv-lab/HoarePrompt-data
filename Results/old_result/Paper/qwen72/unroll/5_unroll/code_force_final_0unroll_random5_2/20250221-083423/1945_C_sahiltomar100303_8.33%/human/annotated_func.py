#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case contains an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident who wants to live on the left side and '1' indicates a resident who wants to live on the right side. The function should also handle an integer `t` (1 ≤ t ≤ 2·10^4) representing the number of test cases. The sum of `n` over all test cases does not exceed 3·10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        mid = n // 2
        
        leftZero = 0
        
        rightZero = 0
        
        leftOne = 0
        
        rightOne = 0
        
        tleftZero = 0
        
        trightZero = 0
        
        tleftOne = 0
        
        trightOne = 0
        
        for i in range(mid):
            if s[i] == '0':
                leftZero += 1
                tleftZero += 1
            else:
                leftOne += 1
                tleftOne += 1
        
        for i in range(mid, n):
            if s[i] == '0':
                rightZero += 1
                trightZero += 1
            else:
                rightOne += 1
                trightOne += 1
        
        left = mid
        
        leftMove = 0
        
        while left > 0 and (leftZero < (left + 1) // 2 or rightOne < (n - left + 1) //
            2):
            if s[left - 1] == '0':
                leftZero -= 1
                rightZero += 1
            else:
                leftOne -= 1
                rightOne += 1
            left -= 1
        
        right = mid
        
        while right < n and (tleftZero < (right + 1) // 2 or trightOne < (n - right +
            1) // 2):
            if s[right] == '0':
                tleftZero += 1
                trightZero -= 1
            else:
                tleftOne += 1
                trightOne -= 1
            right += 1
        
        if left == 0:
            if right != n:
                print(right)
            elif rightOne >= (n + 1) // 2:
                print(left)
            else:
                print(right)
        elif right == n:
            if tleftZero >= (n + 1) // 2:
                print(right)
            else:
                print(left)
        elif abs((n + 1) // 2 - left) <= abs((n + 1) // 2 - right):
            print(left)
        else:
            print(right)
        
    #State: The loop will have processed all `t` test cases, and for each test case, it will have printed the optimal position `left` or `right` where the number of residents on each side is as balanced as possible. The variables `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, `trightOne`, `left`, `leftMove`, and `right` will have been reset or modified for each test case, but their final values will be the result of the last test case processed. The input variables `t`, `n`, and `s` will remain unchanged as they are read from input for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves an integer `n` and a string `s` of length `n` consisting of '0's and '1's. The function calculates and prints the optimal position (either `left` or `right`) for each test case, where the number of residents on each side of the street is as balanced as possible. The function does not return any values; it only prints the results. After processing all test cases, the input variables `t`, `n`, and `s` remain unchanged, but the internal variables used for calculations will have been modified and reset for each test case.

