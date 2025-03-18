#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses. The next line contains a string a of length n, consisting only of 0s and 1s, where a_j = 0 if the resident of the j-th house wants to live on the left side of the street, and a_j = 1 if the resident wants to live on the right side. The sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: t test cases, each consisting of an integer n (3 ≤ n ≤ 3·10^5) and a string a of length n consisting only of 0s and 1s, with the results of each test case printed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the number of houses and a string `a` of length `n` indicating the side preference (0 for left, 1 for right) of each resident. For each test case, it determines and prints the optimal split point in the list of houses such that the number of residents preferring each side is as balanced as possible around this point.

