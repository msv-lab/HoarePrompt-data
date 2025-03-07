#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴. The sequence p is a permutation of {0, 1, ..., n-1}.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10³, `n` is an integer greater than 1, `p` is a permutation of {0, 1, ..., n-1}, `I` is a lambda function, `R` is a lambda function, `g` is 0, `v1` is the largest index i for which r == '<' was observed in the last test case, `prev` is the largest index i for which r == '>' was observed in the last test case, `i` is n-1, `kp` is t-1.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a permutation `p` of the set {0, 1, ..., n-1}. For each test case, it outputs two indices based on comparisons made through an interactive query mechanism.

