#State of the program right berfore the function call: The input consists of an integer t (1 \le t \le 10^4) representing the number of test cases. For each test case, there is an integer n (1 \le n \le 2\cdot 10^5) representing the number of piles, followed by n integers a_1, a_2, \ldots, a_n (1 \le a_i \le 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2\cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        s.sort()
        
        s = [0] + s
        
        ans = 1
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans ^= 1
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the input is processed as follows: `n` is the number of piles, and `arr` is a list of integers representing the number of stones in each pile. The set `s` is created from `arr`, sorted, and prefixed with `0`. If `s` has only two elements, `Alice` is printed. Otherwise, `ans` is determined by iterating through `s` and checking the differences between consecutive elements. If any difference is greater than 1, the loop breaks. If `ans` is 1 after the loop, `Alice` is printed; otherwise, `Bob` is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of piles and the number of stones in each pile. For each test case, it determines the winner of a game based on specific conditions involving the differences between the sorted unique stone counts. The result for each test case is printed, indicating either "Alice" or "Bob" as the winner.

