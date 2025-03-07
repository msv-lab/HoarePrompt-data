#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5; the list a contains n integers such that 1 ≤ a_i ≤ n and each integer from 1 through n appears in a at most twice; the sum of all n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = [0] * (n + 1)
        
        for x in a:
            cnt[x] += 1
        
        ans = 0
        
        for x in cnt:
            ans += max(0, x - 1)
        
        print(ans)
        
    #State: Output State: The value of `ans`, which is the sum of the maximum values of 0 and `x-1` for each element `x` in the list `cnt`. Here, `cnt` is an array where each index `i` (from 1 to n) holds the count of how many times `i` appears in the list `a`. The value of `ans` is calculated by iterating through `cnt` and adding `max(0, x-1)` for each `x` in `cnt`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and a list \( a \) of length \( n \). It then counts the occurrences of each integer in \( a \) and calculates the sum of the maximum values of 0 and \( x-1 \) for each count \( x \). Finally, it prints the calculated sum for each test case.

