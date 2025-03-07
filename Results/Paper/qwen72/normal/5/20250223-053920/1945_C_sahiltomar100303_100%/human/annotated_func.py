#State of the program right berfore the function call: The function is designed to handle multiple test cases. Each test case includes an integer n (3 ≤ n ≤ 3·10^5) representing the number of houses, and a string a of length n consisting only of 0 and 1, where 0 indicates a resident's preference to live on the left side and 1 indicates a preference to live on the right side. The total sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: The output state after the loop executes all the iterations is that the program will have printed the optimal position for dividing the houses into two sides for each test case, ensuring that the number of residents on each side is as balanced as possible according to their preferences. The variables `t`, `n`, `s`, `mid`, `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, `trightOne`, `left`, `leftMove`, and `right` will have been updated and used during the loop execution, but their final values will not be directly relevant to the output state. The output state is the printed result for each test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the input. Each test case consists of an integer `n` (3 ≤ n ≤ 3·10^5) and a string `a` of length `n` containing only '0' and '1'. The function calculates and prints the optimal position to divide the houses into two sides such that the number of residents preferring each side is as balanced as possible. The output for each test case is the index of the house that divides the string into two parts, ensuring the preferences are balanced. If no such perfect balance can be achieved, the function prints the position that is closest to achieving this balance.

