#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a (length n) represents the initial number of stones in each pile, with each a_i satisfying 1 ≤ a_i ≤ 10^9. The sum of all n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: Alice or Bob will be printed based on the input values for each test case. For each test case, if there exists an index `i` (1 < i < n-1) where `s[i] - s[i-1] > 1`, the loop breaks and "Alice" is printed. Otherwise, if `ans` is 1, "Alice" is printed; otherwise, "Bob" is printed. The specific output depends on the input values for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n and a list of n integers representing the initial number of stones in each pile. For each test case, it determines whether Alice or Bob wins based on the sorted unique stone counts. If there is a gap greater than 1 between any two consecutive piles, Alice wins; otherwise, Bob wins. The function prints "Alice" or "Bob" for each test case.

