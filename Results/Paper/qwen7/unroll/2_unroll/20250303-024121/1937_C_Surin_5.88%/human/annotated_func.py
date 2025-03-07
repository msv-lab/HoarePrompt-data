#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 2 ≤ n ≤ 10^4. Additionally, p is a permutation of integers from 0 to n-1, and the interactor is not adaptive.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^3, and for each test case, `n` is an integer such that 2 ≤ n ≤ 10^4; `R` is a lambda function that takes input, splits it by spaces, and maps each element to an integer; after all iterations, `prev` is the smallest index `i` (1 ≤ i < n) such that the comparison `? v1 i v1 prev` returns '>', and `v1` is the value initialized as 0.
    #
    #In simpler terms, `prev` is the smallest index where the value at that index is greater than the value at `v1`, and `v1` remains 0 throughout the process.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` such that 2 ≤ n ≤ 10^4. For each test case, it initializes `v1` to 0 and iterates through indices from 1 to n-1. It compares the value at index `v1` with the value at each index `i` and updates `v1` and another variable `prev` based on the comparison results. After completing the comparisons, it outputs the value of `prev`, which is the smallest index `i` (1 ≤ i < n) where the value at that index is greater than the value at `v1`. The function does not return any value but prints the result for each test case.

