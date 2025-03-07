#State of the program right berfore the function call: The function operates in an interactive environment where the input sequence is a permutation of integers from 0 to n-1, and n is an integer such that 2 ≤ n ≤ 10^4. The function can make at most 3n queries, and each query involves four indices a, b, c, d (0 ≤ a, b, c, d < n). The goal is to find two indices i and j (0 ≤ i, j < n) such that p_i ⊕ p_j is maximized.
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
        
    #State: The loop will output two indices `maxi` and `mini` such that the XOR of the elements at these indices in the permutation `p` is maximized. The variables `maxi` and `mini` will hold the indices of the elements in the permutation `p` that achieve this maximum XOR value. The list `arr` will contain all indices `i` such that `p_i ⊕ p_maxi` is equal to the maximum XOR value found during the loop execution.
#Overall this is what the function does:The function operates in an interactive environment and processes a series of permutations of integers from 0 to n-1, where 2 ≤ n ≤ 10^4. For each permutation, it makes at most 3n queries involving four indices each. The function identifies and outputs two indices `maxi` and `mini` such that the XOR of the elements at these indices in the permutation `p` is maximized. The list `arr` will contain all indices `i` such that `p_i ⊕ p_maxi` is equal to the maximum XOR value found during the loop execution.

