#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists, where each inner list contains n integers (1 ≤ n ≤ 2·10^5) representing the number of stones in each pile for a test case. Each integer in the inner lists (a_i) is in the range 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The loop will iterate through each test case, and for each test case, it will determine whether Alice or Bob wins based on the conditions provided in the loop. After all iterations, the output state will be the results of the test cases printed as 'Alice' or 'Bob' for each test case. The variables `t` and the list of lists will remain unchanged, while the variables `n`, `arr`, `s`, and `ans` will have their values modified during each iteration of the loop but will be reset for the next test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, and for each test case, it reads an integer `n` followed by a list of `n` integers from the input, representing the number of stones in each pile. The function then determines and prints whether Alice or Bob wins for each test case based on the conditions provided in the loop. The function does not return any value; it only prints the results. After all test cases are processed, the input state (the integer `t` and the list of lists) remains unchanged, but the internal variables used within the function (`n`, `arr`, `s`, and `ans`) are reset for each test case.

