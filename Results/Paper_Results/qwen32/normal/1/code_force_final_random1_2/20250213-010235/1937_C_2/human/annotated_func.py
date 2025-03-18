#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4, and p is a permutation of the set {0, 1, ..., n-1}. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: 
#Overall this is what the function does:For each test case, the function determines and prints a pair of indices from the given permutation `p` of the set {0, 1, ..., n-1}. Specifically, it identifies two indices `k` and `best` and outputs them, likely representing a specific relationship or comparison result within the permutation.

