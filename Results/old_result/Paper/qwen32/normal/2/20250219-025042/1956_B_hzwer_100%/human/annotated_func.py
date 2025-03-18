#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The total number of test cases t (1 ≤ t ≤ 10^4) is provided at the start, and the sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: 1
#Overall this is what the function does:The function processes multiple test cases where each test case consists of a number of cards `n` and a list of integers representing the cards. For each test case, it calculates the number of duplicate cards and prints this count.

