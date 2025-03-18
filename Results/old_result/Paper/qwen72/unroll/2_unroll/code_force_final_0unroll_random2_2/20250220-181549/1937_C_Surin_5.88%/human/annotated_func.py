#State of the program right berfore the function call: The function is part of an interactive problem where the input is a sequence of test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation of integers from 0 to n-1. The function can make at most 3n queries to find two indices i and j (0 ≤ i, j < n) such that the bitwise XOR of p_i and p_j is maximized. The total sum of n over all test cases does not exceed 10^4.
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
        
    #State: For each test case, the loop outputs two indices `prev` and `v1` such that the bitwise XOR of the elements at these indices in the permutation is maximized. The loop iterates through all test cases, and for each test case, it queries the input to find these indices and then prints them in the format `! {prev} {v1}`. After all iterations, the variables `kp`, `n`, `g`, `v1`, and `prev` will have their final values corresponding to the last test case processed. The total number of queries made for all test cases will not exceed the allowed limit of 3n.
#Overall this is what the function does:The function `func` processes a sequence of test cases, each with an integer `n` (2 ≤ n ≤ 10^4). For each test case, it interacts with an external system by making at most 3n queries to find two indices `prev` and `v1` such that the bitwise XOR of the elements at these indices in the permutation is maximized. After finding these indices, it prints them in the format `! {prev} {v1}`. The function does not explicitly accept any parameters and does not return any values. After processing all test cases, the variables `kp`, `n`, `g`, `v1`, and `prev` will hold their final values corresponding to the last test case processed.

