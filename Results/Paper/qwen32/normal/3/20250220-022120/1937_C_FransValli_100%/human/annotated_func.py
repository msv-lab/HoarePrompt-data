#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a secret permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. For each test case, the function can interactively query up to 3n times to compare the bitwise OR of pairs of elements in the permutation, and must then output a pair of indices i and j such that the bitwise XOR of p_i and p_j is maximized. The sum of n across all test cases does not exceed 10^4.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        maxi = 0
        
        for i in range(1, n):
            print('?', maxi, maxi, i, i, flush=True)
            res = input()
            if res == '<':
                maxi = i
        
        arr = [0]
        
        for i in range(1, n):
            print('?', maxi, arr[0], maxi, i, flush=True)
            res = input()
            if res == '<':
                arr = [i]
            elif res == '=':
                arr.append(i)
        
        mini = arr[0]
        
        for item in arr[1:]:
            print('?', mini, mini, item, item, flush=True)
            res = input()
            if res == '>':
                mini = item
        
        print('!', maxi, mini, flush=True)
        
    #State: maxi, mini for the last test case processed.
#Overall this is what the function does:The function interacts with the environment to query up to 3n times for each test case, comparing the bitwise OR of pairs of elements in a secret permutation of length n. Based on these queries, it identifies and returns a pair of indices (i, j) such that the bitwise XOR of the elements at these indices in the permutation is maximized.

