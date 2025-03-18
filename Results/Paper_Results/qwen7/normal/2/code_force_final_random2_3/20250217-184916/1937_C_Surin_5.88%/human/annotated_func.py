#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires interacting with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \) which is a permutation of \(\{0, 1, \ldots, n-1\}\), and allows asking up to \(3n\) queries of the form "? a b c d" to determine the indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized.
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
        
    #State: The loop will have executed for all provided inputs, with the following conditions:
#Overall this is what the function does:The function interacts with a hidden permutation of numbers from 0 to n-1. It asks up to 3n queries of the form "? a b c d" to find the indices i and j such that the bitwise XOR of the elements at these indices (p_i ⊕ p_j) is maximized. For each input, the function determines and outputs the indices i and j that satisfy this condition.

