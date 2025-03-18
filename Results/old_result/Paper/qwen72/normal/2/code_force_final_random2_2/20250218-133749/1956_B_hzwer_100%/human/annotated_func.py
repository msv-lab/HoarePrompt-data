#State of the program right berfore the function call: t is an integer representing the number of test cases, where 1 ≤ t ≤ 10^4. For each test case, n is an integer representing the number of cards each player receives, where 1 ≤ n ≤ 2 · 10^5. a_1, a_2, ..., a_n are integers representing the numbers on the cards in your hand, where 1 ≤ a_i ≤ n, and each integer from 1 to n appears at most twice in the sequence. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all the iterations, `t` is an integer where 1 ≤ t ≤ 10^4, and for each of the `t` test cases, the following holds: `n` is an integer greater than 0, `a` is a list of integers with `len(a)` elements, `cnt` is a list of length `n + 1` where each element `cnt[i]` represents the count of occurrences of the integer `i` in the list `a`, and `ans` is the sum of `max(0, x - 1)` for all elements `x` in `cnt`. Each `ans` value is printed for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case involves a set of cards represented by integers. It calculates the number of cards that appear more than once in each test case and prints this count for each test case. The function processes up to \(10^4\) test cases, where each test case can have up to \(2 \times 10^5\) cards. After processing all test cases, the function has printed the count of duplicate cards for each test case.

