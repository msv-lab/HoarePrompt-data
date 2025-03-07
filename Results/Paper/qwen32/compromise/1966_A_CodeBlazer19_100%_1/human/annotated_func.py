#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. The list c contains n integers where each integer c_i satisfies 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: A series of integers, one for each test case, where each integer is either `k - 1` if the maximum frequency of any integer in the list is at least `k`, or `n` otherwise.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it determines whether the highest frequency of any integer in a given list of integers is at least a specified value `k`. If so, it outputs `k - 1`; otherwise, it outputs the length of the list `n`.

