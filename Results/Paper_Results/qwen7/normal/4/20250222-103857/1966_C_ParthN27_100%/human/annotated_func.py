#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the initial number of stones in each pile. It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: All iterations of the loop have completed. The variable `i` is equal to `n`, `s` is a sorted list of all unique elements from the list `arr` with an additional 0 at the beginning, `n` is the length of `s`, and `ans` is 1. If the length of `s` is 2, the postcondition remains as described. If the length of `s` is not 2, `i` is 3, and `ans` remains 1.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` indicating the number of piles, followed by `n` integers representing the number of stones in each pile. It then determines whether Alice or Bob wins based on the sorted unique values of the stones in the piles. If the length of the sorted unique values is 2, it prints 'Alice'. Otherwise, it checks if the difference between consecutive elements is greater than 1; if so, it prints 'Alice', otherwise it prints 'Bob'. The function does not return any value but prints the result for each test case.

