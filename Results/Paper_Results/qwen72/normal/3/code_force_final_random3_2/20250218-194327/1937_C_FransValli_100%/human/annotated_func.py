#State of the program right berfore the function call: The function operates in an interactive environment where the input is a sequence of test cases, each with a permutation of integers from 0 to n-1, and the function can make at most 3n queries to find a pair of indices (i, j) such that p_i ⊕ p_j is maximized. The number of test cases t satisfies 1 ≤ t ≤ 10^3, and for each test case, n satisfies 2 ≤ n ≤ 10^4. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: After all iterations, `n` remains unchanged, `i` is `n-1`, `maxi` is the index of the element in the permutation that, when XORed with itself, results in the maximum value among all such XOR operations, `arr` contains the indices of all elements that, when XORed with `maxi`, resulted in a value that is either equal to or less than the current maximum, and `mini` is the index of the element in `arr` that, when XORed with `maxi`, results in the minimum value among all such XOR operations. `item` is the last element of `arr` that was processed.
#Overall this is what the function does:The function operates in an interactive environment to process a series of test cases. For each test case, it takes an integer `n` as input, representing the length of a permutation of integers from 0 to n-1. The function then interacts with the environment by making queries to find a pair of indices (i, j) such that the bitwise XOR of the elements at these indices, p_i ⊕ p_j, is maximized. After processing all test cases, the function outputs the pairs of indices (i, j) for each test case. The function can handle up to 10^3 test cases, with each permutation length n ranging from 2 to 10^4, and the sum of n over all test cases not exceeding 10^4. The final state of the program after the function concludes is that all test cases have been processed, and the pairs of indices that maximize the XOR operation have been outputted.

