#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n is an integer such that 2 ≤ n ≤ 10^4, and there exists a secret permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: t is unchanged, n is unchanged, kp is equal to t, g is 0, v1 is the last determined maximum element, v2 is n-1, prev is the last determined second maximum element.
#Overall this is what the function does:The function processes multiple test cases, each involving a secret permutation of integers from 0 to n-1. For each test case, it interacts with an external system to determine and output the second largest and the largest elements in the permutation.

