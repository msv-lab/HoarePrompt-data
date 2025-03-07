#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and the input consists of t test cases. For each test case, n is the number of cards you and Nene receive initially, and the second line contains n integers a_1, a_2, \ldots, a_n such that 1 ≤ a_i ≤ n and each integer from 1 through n appears at most 2 times in the sequence.
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
        
    #State: Output State: t test cases printed, each followed by an integer representing the maximum number of pairs of identical numbers that can be formed from the input list a by decrementing each element by one until no two elements are the same in the list.
#Overall this is what the function does:The function processes up to 10,000 test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then counts the occurrences of each integer in the list and calculates the maximum number of pairs of identical numbers that can be formed by decrementing each element by one until no two elements are the same. Finally, it prints the result for each test case, which is the total count of such pairs.

