#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2 · 10^5) representing the number of cards each player receives. This is followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the integers on the cards in your hand. Each integer from 1 through n appears in the sequence a_1, a_2, ..., a_n at most 2 times. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The output state consists of the printed answers for each test case, which are the sums of the excess counts of each integer in their respective test cases.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes a number `n` and a list of `n` integers. It calculates the sum of excess counts for each integer in the list (i.e., the number of times each integer appears more than once) and prints this sum for each test case.

