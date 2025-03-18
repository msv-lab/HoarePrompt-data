#State of the program right berfore the function call: This is an interactive problem with no explicit input variables in the function signature. However, the precondition includes the existence of a secret permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \( \{0, 1, \ldots, n-1\} \), and the ability to make up to \( 3n \) queries comparing bitwise OR results to deduce the indices \( i \) and \( j \) such that \( p_i \oplus p_j \) is maximized.
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
        
    #State: Output State: The output state will consist of two main parts. First, for each iteration of the outer loop (controlled by `kp`), the code will determine the relative order of elements using comparisons. Specifically, it will identify two indices, `prev` and `v1`, which represent the positions of the smallest and second smallest elements in the array, respectively. Second, the code will output these indices in the format `! prev v1`. After all iterations, the output state will contain these pairs of indices for each `kp` value, indicating the relative ordering of the smallest and second smallest elements found during each iteration.
#Overall this is what the function does:The function determines the indices of the smallest and second smallest elements in a secret permutation of \(\{0, 1, \ldots, n-1\}\) through up to \(3n\) comparisons. For each iteration controlled by `kp`, it identifies two indices, `prev` and `v1`, representing the smallest and second smallest elements, respectively. After all iterations, it outputs these pairs of indices in the format `! prev v1`, indicating the relative ordering of the smallest and second smallest elements found during each iteration.

