#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a (length n) represents the initial number of stones in each pile, with 1 ≤ a_i ≤ 10^9 for each pile. The sum of all n over all test cases does not exceed 2⋅10^5.
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
        
    #State: The loop has executed for all test cases, and for each test case: `i` is equal to `n-1`, `s` is a sorted list containing all unique elements from the list `arr` with 0 at the beginning, and `ans` is either 1 if `n` is exactly 2, or 0 if `n` is at least 3.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer \( t \) (number of piles), a positive integer \( n \) (number of stones in each pile), and a list of \( n \) integers representing the initial number of stones in each pile. For each test case, the function determines whether Alice or Bob wins based on the initial distribution of stones and prints the winner.

