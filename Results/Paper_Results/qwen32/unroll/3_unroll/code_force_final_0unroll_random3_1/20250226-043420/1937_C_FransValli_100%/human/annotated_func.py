#State of the program right berfore the function call: There are multiple test cases, each with an integer n (2 ≤ n ≤ 10^4) representing the length of a permutation p_0, p_1, ..., p_{n-1} of the set {0, 1, ..., n-1}. The function can interactively query up to 3n times per test case to compare bitwise OR results of pairs of elements in the permutation, and must output a pair of indices i and j such that p_i ⊕ p_j is maximized. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: For each test case, the indices `maxi` and `mini` are printed such that `p_maxi ⊕ p_mini` is maximized.
#Overall this is what the function does:The function interacts with an external system to determine a pair of indices in a permutation of integers from 0 to n-1 such that the bitwise XOR of the elements at these indices is maximized. For each test case, it outputs the indices that achieve this maximum XOR value.

