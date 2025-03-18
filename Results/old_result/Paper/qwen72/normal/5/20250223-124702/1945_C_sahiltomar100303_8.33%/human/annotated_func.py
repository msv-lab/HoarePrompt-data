#State of the program right berfore the function call: The function `func` is intended to process multiple test cases, each containing a single integer `n` (3 ≤ n ≤ 3·10^5) and a string `a` of length `n` consisting only of '0' and '1'. The number of test cases `t` is an integer (1 ≤ t ≤ 2·10^4), and the sum of `n` over all test cases does not exceed 3·10^5.
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
        
    #State: The loop processes each test case and prints the optimal position to split the string `s` into two parts such that the number of '0's in the left part and the number of '1's in the right part are as close as possible to half of the length of the string. After all iterations, the variables `t`, `n`, and `s` will have been used and reset for each test case, but the values of `t` provided by the user will remain unchanged. The internal variables `mid`, `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, `trightOne`, `left`, `leftMove`, and `right` will be reset and used for each test case, and their final values will depend on the last test case processed.
#Overall this is what the function does:The function `func` processes multiple test cases, each with an integer `n` and a string `s` of length `n` containing only '0' and '1'. For each test case, it calculates and prints the optimal position to split the string `s` such that the number of '0's in the left part and the number of '1's in the right part are as close as possible to half of the length of the string. After processing all test cases, the function does not return any value, but the results for each test case are printed to the console. The variables `t`, `n`, and `s` are used and reset for each test case, and their final values are not retained after the function completes. The internal variables used for calculations are reset for each test case and their final values depend on the last test case processed.

