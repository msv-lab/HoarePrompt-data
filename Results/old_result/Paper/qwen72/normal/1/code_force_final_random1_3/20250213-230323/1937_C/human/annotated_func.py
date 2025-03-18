#State of the program right berfore the function call: The function operates in an environment where it can interactively query a judge to compare bitwise OR results of elements from a hidden permutation of integers from 0 to n-1. The function must find a pair of indices (i, j) such that the bitwise XOR of the elements at these indices is maximized, using no more than 3n queries. The input n is an integer where 2 ≤ n ≤ 10^4, and the total sum of n across all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: After all iterations of the loop, `n` remains the same as the initial input integer, `i` is `n-1`, `k` is the index that resulted in the maximum bitwise OR when compared with 0, and `best` is the index that resulted in the maximum bitwise OR when compared with `k`. The variable `res` holds the last input string received from the judge.
#Overall this is what the function does:The function interacts with an environment that provides a hidden permutation of integers from 0 to n-1. It queries a judge to compare bitwise OR results of elements from this permutation, aiming to find a pair of indices (i, j) such that the bitwise XOR of the elements at these indices is maximized. The function uses no more than 3n queries to achieve this. After the function completes, it outputs the pair of indices (k, best) that result in the maximum bitwise XOR. The variables `n`, `k`, `best`, and `res` retain their final values from the last iteration, with `n` being the input integer, `k` and `best` being the indices found, and `res` holding the last response from the judge.

