#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n is an integer such that 2 <= n <= 10^4, and p is a permutation of the integers from 0 to n-1. The sum of n over all test cases does not exceed 10^4.
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
            elif r == '=':
                print(f'? {i} {i} {prev} {prev}')
                sys.stdout.flush()
                r2 = input('')
                if r2 == '<':
                    prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: `v1` is the index of the smallest element in the permutation for the last test case, and `prev` is the index of the second smallest element in the permutation for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a permutation `p` of integers from 0 to `n-1`. For each test case, it determines the indices of the smallest and second smallest elements in the permutation and outputs these indices.

