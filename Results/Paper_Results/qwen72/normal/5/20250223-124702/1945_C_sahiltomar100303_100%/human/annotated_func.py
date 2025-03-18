#State of the program right berfore the function call: The function `func` is expected to be called within a context where multiple test cases are provided. Each test case includes an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident's preference to live on the left side of the road, and '1' indicates a preference to live on the right side. The function should handle these inputs internally and is expected to be called in a loop or similar structure to process each test case. The total sum of `n` over all test cases does not exceed 3·10^5.
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
            if left != 0:
                print(left)
            elif tleftZero >= (n + 1) // 2:
                print(right)
            else:
                print(left)
        elif abs((n + 1) // 2 - left) <= abs((n + 1) // 2 - right):
            print(left)
        else:
            print(right)
        
    #State: The loop will have processed all `t` test cases, and for each test case, it will have printed the optimal position `left` or `right` where the number of residents living on their preferred side of the road is maximized. The variables `n`, `s`, `mid`, `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, `trightOne`, `left`, `leftMove`, and `right` will be reset or updated for each new test case, but the overall number of test cases `t` will remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` (3 ≤ n ≤ 3·10^5) and a string `a` of length `n` containing only '0' and '1'. The function calculates and prints the optimal position (either `left` or `right`) where the number of residents living on their preferred side of the road is maximized. The function does not return any value; it only prints the result for each test case. The state of the program after the function concludes includes all test cases being processed and the optimal positions printed for each. The variables used within the function are reset or updated for each new test case, but the total number of test cases `t` remains unchanged.

