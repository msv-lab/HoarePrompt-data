#State of the program right berfore the function call: n and k are integers such that 2 <= k <= n and k is even.
def func_1():
    n, k = map(int, input().split(' '))
    permutation = [0] * n
    idx = 0
    idx_v = 1
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
        
    #State: permutation is [1, 4, 7, 9, 2, 5, 8, 10, 3, 6], idx is 0, idx_v is 1, curr_v is 11.
    result = ' '.join([str(v) for v in permutation])
    print(result)
    #This is printed: 1 4 7 9 2 5 8 10 3 6
#Overall this is what the function does:The function generates a permutation of integers from 1 to `n` based on the specified rules involving `k` and prints the result as a space-separated string.

