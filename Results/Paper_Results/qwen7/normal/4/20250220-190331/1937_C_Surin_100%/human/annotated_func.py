#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \(\{0, 1, \ldots, n-1\}\). The function can ask up to \(3n\) queries to compare bitwise OR results and determine the indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized.
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
        
    #State: Output State: The loop has executed all its iterations, with `i` reaching `n`. The value of `n` must be greater than or equal to 3. After the loop completes, `v1` will be `n-1`, `v2` will be `n-1`, and `prev` will be `n`. All necessary `sys.stdout.flush()` calls have been made to ensure proper execution flow.
#Overall this is what the function does:The function interacts with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \) and determines the indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized. It does this by making up to \(3n\) queries to compare bitwise OR results. After completing the loop, the function outputs the indices \(i\) and \(j\) that maximize the bitwise XOR operation.

