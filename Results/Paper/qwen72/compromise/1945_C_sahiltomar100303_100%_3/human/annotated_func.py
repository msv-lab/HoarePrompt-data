#State of the program right berfore the function call: The function is designed to handle multiple test cases. Each test case includes an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string a of length n consisting only of '0' and '1', where '0' indicates a resident wanting to live on the left side and '1' indicates a resident wanting to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: `_` is `t - 1`, `n` is an input integer, `s` is an input string, `mid` is `n // 2`, `leftZero` is 0, `rightZero` is 0, `leftOne` is `tleftOne + (n // 2)`, `rightOne` is 0, `tleftZero` is the number of '0's in the first half of `s`, `tleftOne` is the number of '1's in the first half of `s`, `trightZero` is the number of '0's in the second half of `s`, `trightOne` is the number of '1's in the second half of `s`, `leftMove` is 0, `left` is either 0 or not 0, `right` is `n`.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` (3 ≤ n ≤ 3·10^5) and a string `s` of length `n` consisting of '0' and '1'. The function calculates and prints the optimal position to divide the string `s` into two halves such that the number of '0's and '1's on each side is as balanced as possible, according to the residents' preferences. The function does not return any value; instead, it prints the result for each test case. After the function concludes, the state of the program includes the processed test cases and the printed optimal positions for each test case.

