#State of the program right berfore the function call: The function is expected to handle multiple test cases. Each test case includes an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string a of length n consisting only of '0' and '1', where '0' indicates a resident who wants to live on the left side and '1' indicates a resident who wants to live on the right side. The total sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: The loop will have processed all test cases, and for each test case, it will have printed the optimal boundary index (left or right) that balances the number of '0's and '1's as close to the middle as possible, given the constraints. The variables `t`, `n`, `s`, `mid`, `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, `trightOne`, `left`, `leftMove`, and `right` will have been updated and used during the execution of the loop, but their final values will depend on the specific inputs provided for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case consists of an integer `n` and a string `s` of length `n` containing only '0' and '1'. The function calculates and prints the optimal boundary index (either `left` or `right`) that balances the number of '0's and '1's as close to the middle of the string as possible, given the constraints. The boundary index is the position where the number of '0's on the left and '1's on the right is as balanced as possible. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function concludes, and the final state of the program is that all test cases have been processed and the optimal boundary indices have been printed for each.

