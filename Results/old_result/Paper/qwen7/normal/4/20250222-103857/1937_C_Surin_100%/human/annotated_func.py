#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem requires the function to interact with an external entity to perform queries and determine the maximum XOR value of any two indices in a hidden permutation. The function must handle up to 3n queries, where n is the size of the permutation, and n ranges from 2 to 10^4.
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
        
    #State: The loop has completed all its iterations. The value of `n` is greater than 3, `i` is `n`, `v2` is `n-1`, `v1` is `n-1`, `prev` is either `n-1` or `n-2` based on user inputs, and `g` remains 0.
#Overall this is what the function does:The function interacts with an external entity to perform queries and determines the maximum XOR value of any two indices in a hidden permutation. It handles up to 3n queries, where n is the size of the permutation (ranging from 2 to 10^4). After completing all iterations, it outputs the maximum XOR value found.

