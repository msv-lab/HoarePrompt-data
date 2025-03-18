#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴. The sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}. The sum of n over all test cases does not exceed 10⁴.
def func():
    I = lambda : list(map(int, input().split(' ')))
    R = lambda : int(input())
    for kp in range(int(input())):
        n = int(input())
        
        g = 0
        
        v1 = 0
        
        for i in range(1, n):
            v2 = i
            print(f'? {v1} {v1} {v2} {v2}')
            sys.stdout.flush()
            r = input('')
            if r == '<':
                v1 = v2
        
        prev = 0
        
        for i in range(1, n):
            print(f'? {v1} {i} {v1} {prev}')
            sys.stdout.flush()
            r = input()
            if r == '>':
                prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: kp is equal to t, n is the integer from the last test case, g is 0, v1 is the largest index i for which the input r was '<' in the last test case, prev is the largest index i for which the input r was '>' in the last test case, i is n, v2 is n-1, r is the input string from the last iteration of the inner loop in the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a permutation `p` of the sequence `{0, 1, ..., n-1}`. For each test case, it outputs two indices based on specific comparisons made through queries. The first index is the largest index `i` for which a certain comparison condition holds true, and the second index is another significant index derived from the permutation.

