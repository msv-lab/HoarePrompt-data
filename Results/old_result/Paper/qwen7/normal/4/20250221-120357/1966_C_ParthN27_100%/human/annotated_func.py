#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a (length n) represents the initial number of stones in each pile, with each a_i satisfying 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: After all iterations of the loop have finished, `n` is equal to the length of `s`, `i` is equal to `n-1`, `arr` remains the same list of integers, `s` is `[0] + s`, and `ans` reflects the final toggle state based on the sequence in `s`. If the length of `s` is 2, `i` is `n-1` and `ans` is 1. If the length of `s` is greater than 2, `i` will be between `n-2` and 1 (inclusive), and `ans` will be 1 if the number of iterations is even, or 0 if the number of iterations is odd.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers representing the number of stones in each pile. It then determines whether Alice or Bob wins based on the distribution of stones. Specifically, it checks if the difference between consecutive elements in the sorted unique list of stones is more than 1. If the number of such differences is even, Alice wins; otherwise, Bob wins. The function prints 'Alice' or 'Bob' for each test case.

