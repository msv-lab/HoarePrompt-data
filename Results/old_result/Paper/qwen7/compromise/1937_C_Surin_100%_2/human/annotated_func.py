#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with an external entity to determine the permutation \( p_0, p_1, \ldots, p_{n-1} \) through a series of queries. The input variables are the number of test cases \( t \) and for each test case, the size of the permutation \( n \).
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
        
    #State: The loop will execute until all possible comparisons are made, with `i` reaching `n`, `n` being at least 6, `v2` being `n-1`, `v1` being `n-1`, and `prev` being `n-1`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it determines the permutation \( p_0, p_1, \ldots, p_{n-1} \) of size \( n \) through a series of queries to an external entity. It does not return any value but prints the determined permutation for each test case.

