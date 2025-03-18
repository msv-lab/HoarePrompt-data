#State of the program right berfore the function call: The function should be called with a list of test cases, where each test case is a tuple containing an integer n (3 ≤ n ≤ 3·10^5) and a string a of length n consisting only of '0' and '1'. The total sum of n over all test cases does not exceed 3·10^5.
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
        
    #State: The loop will have processed all test cases, and the output will be the positions (1-indexed) where the string can be split such that the left part has at least half of its length as '0's and the right part has at least half of its length as '1's. The variables `left`, `right`, `leftZero`, `rightZero`, `leftOne`, `rightOne`, `tleftZero`, `trightZero`, `tleftOne`, and `trightOne` will be in their final states after processing the last test case.
#Overall this is what the function does:The function `func` processes a series of test cases, each consisting of an integer `n` and a string `a` of length `n` containing only '0' and '1'. For each test case, it calculates and prints the position (1-indexed) where the string can be split such that the left part has at least half of its length as '0's and the right part has at least half of its length as '1's. If no such split is possible, it prints the position that minimizes the difference from the ideal split. The function does not return any value; it only prints the results. After processing all test cases, the function concludes, and the state of the program includes the final values of the variables used in the last test case.

