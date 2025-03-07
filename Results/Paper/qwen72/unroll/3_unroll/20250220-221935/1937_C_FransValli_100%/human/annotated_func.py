#State of the program right berfore the function call: The function operates in an interactive environment where the input is a sequence of queries and responses. The sequence p is a permutation of {0, 1, ..., n-1} where 2 ≤ n ≤ 10^4. The function can make at most 3n queries, and each query involves four indices a, b, c, d (0 ≤ a, b, c, d < n). The response to each query is one of "<", "=", or ">", indicating the result of the comparison between (p_a | p_b) and (p_c | p_d). The function must find and output a pair of indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop will have found and printed a pair of indices (maxi, mini) such that the XOR of the elements at these indices in the permutation p is maximized. The variables `maxi` and `mini` will hold the indices of the elements in the permutation p that achieve this maximum XOR value.
#Overall this is what the function does:The function operates in an interactive environment to find and print a pair of indices (maxi, mini) from a permutation sequence p, such that the bitwise XOR of p[maxi] and p[mini] is maximized. The function takes no parameters and reads input values interactively. After processing, it prints the pair of indices (maxi, mini) that achieve the maximum XOR value. The variables `maxi` and `mini` will hold the indices of the elements in the permutation p that achieve this maximum XOR value.

