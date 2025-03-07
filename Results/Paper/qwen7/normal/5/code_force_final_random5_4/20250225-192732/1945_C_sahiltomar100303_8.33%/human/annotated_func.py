#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2⋅10^4. For each test case, n is an integer such that 3 ≤ n ≤ 3⋅10^5, and a is a string of length n consisting only of '0' and '1'. The sum of n over all test cases does not exceed 3⋅10^5.
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
        
    #State: The final state will depend on the initial value of `t` (number of test cases). After processing all iterations, the following conditions will hold:
#Overall this is what the function does:The function processes multiple test cases, each containing a positive integer \( t \), an integer \( n \), and a binary string \( a \) of length \( n \). For each test case, it calculates the number of zeros and ones in the first half and second half of the string. It then determines and prints the position \( p \) (either left or right) that minimizes the absolute difference between the count of zeros and ones when considering the substring starting from the beginning up to position \( p \) or from position \( p \) to the end.

