#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses. This is followed by a string a of length n, consisting only of the characters '0' and '1', where '0' indicates a resident wants to live on the left side and '1' indicates a resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: `t` is 0; `n` is 0; `s` is an empty string; `mid` is 0; `leftZero` is 0; `rightZero` is 0; `leftOne` is 0; `rightOne` is 0; `tleftZero` is 0; `trightZero` is 0; `tleftOne` is 0; `trightOne` is 0; `left` is 0; `right` is 0; `leftMove` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of houses `n` and a string `s` indicating the side preference ('0' for left, '1' for right) of each resident. For each test case, it determines and prints the optimal number of residents that can be accommodated on the left side such that the number of residents on each side is as balanced as possible, with the left side having at least as many residents as the right side if the total number of residents is odd.

