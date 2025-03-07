#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴, and p is a permutation of the set {0, 1, ..., n-1}. The sum of n over all test cases does not exceed 10⁴.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: the output state you calculate.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a permutation `p` of the set {0, 1, ..., n-1}. For each test case, it outputs two integers `k` and `best` that represent specific indices in the permutation `p`. The function interacts with an external system by printing queries and reading responses to determine these indices.

