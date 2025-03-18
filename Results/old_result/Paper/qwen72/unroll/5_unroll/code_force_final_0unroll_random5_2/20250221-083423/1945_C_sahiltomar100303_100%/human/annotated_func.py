#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case contains an integer `n` (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string `a` of length `n` consisting only of '0' and '1', where '0' indicates a resident's preference to live on the left side of the street and '1' indicates a preference to live on the right side. The total number of test cases `t` is such that 1 ≤ t ≤ 2·10^4, and the sum of `n` over all test cases does not exceed 3·10^5.
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
        
    #State: The loop will have processed all test cases, and for each test case, it will have printed a single integer indicating the optimal position of the dividing line between the left and right sides of the street to satisfy the residents' preferences as much as possible. The variables `tleftZero`, `tleftOne`, `trightZero`, and `trightOne` will have been updated to reflect the counts of '0's and '1's on the left and right sides of the street for the last test case processed. The variables `left`, `right`, `leftZero`, `rightZero`, `leftOne`, and `rightOne` will have been reset for each test case, and their final values will be the result of the last test case's computations.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case consists of an integer `n` and a string `a` of length `n` containing only '0's and '1's. The function calculates and prints the optimal position of a dividing line between the left and right sides of the street to maximize the number of residents whose preferences are satisfied. The preferences are indicated by '0' for the left side and '1' for the right side. After processing all test cases, the function will have printed an integer for each test case, representing the optimal position of the dividing line. The internal variables used for calculations will be reset for each test case, and the final state of these variables will reflect the computations of the last test case processed.

