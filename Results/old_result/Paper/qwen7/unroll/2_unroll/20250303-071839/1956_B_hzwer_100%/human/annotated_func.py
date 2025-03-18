#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers a_1, a_2, ..., a_n represents the integers on the cards in your hand, where each integer from 1 through n appears at most twice.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2⋅10^5, and the list of integers `a_1, a_2, ..., a_n` represents the integers on the cards in your hand, where each integer from 1 through n appears at most twice. After executing the loop, the variable `ans` is the sum of the maximum values of 0 and `x-1` for each element `x` in the list `cnt`, where `cnt` is an array counting the occurrences of each integer in `a`.
#Overall this is what the function does:The function processes a series of inputs, each consisting of an integer \( n \) and a list of integers \( a \), where each integer from 1 to \( n \) appears at most twice. For each input, it counts the occurrences of each integer in the list \( a \) and calculates the sum of the maximum values of 0 and \( x-1 \) for each count \( x \). Finally, it prints the calculated sum for each input.

