#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n is an integer such that 2 ≤ n ≤ 10⁴. The sequence p_0, p_1, ..., p_{n-1} is a permutation of {0, 1, ..., n-1}.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10³, n is greater than 1, g is 0, v1 is the index of the maximum element in the array, v2 is n-1, prev is the index of the maximum element in the array, kp is equal to t.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a permutation of integers from `0` to `n-1`. For each test case, it outputs two indices: the first index is the position of the largest element in the permutation, and the second index is also the position of the largest element.

