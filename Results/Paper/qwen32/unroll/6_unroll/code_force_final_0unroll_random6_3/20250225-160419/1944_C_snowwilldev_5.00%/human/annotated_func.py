#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2 · 10^4. For each of the t test cases, n is an integer such that 1 ≤ n ≤ 2 · 10^5, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for tc in range(int(input())):
        N = int(input())
        
        a = list(map(int, input().split()))
        
        cnt = defaultdict(int)
        
        for i in range(N):
            cnt[a[i]] += 1
        
        t = 0
        
        for i in range(N):
            if cnt[i] == 1:
                t += 1
            if t >= 2 or cnt[i] == 0:
                print(i)
                break
        
    #State: A series of integers, each corresponding to the output of one test case, printed one per line.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` and a list `a` of `n` integers where each integer is between 0 and `n-1`. It then determines and prints the smallest integer `i` such that either `i` appears exactly once in the list `a` or `i` does not appear at all in the list `a`. If there are at least two such integers, it prints the first one it encounters.

