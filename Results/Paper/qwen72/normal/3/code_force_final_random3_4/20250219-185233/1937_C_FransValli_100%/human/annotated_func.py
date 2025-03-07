#State of the program right berfore the function call: The function `func` is part of an interactive problem where the input is a sequence of test cases, each with an integer n (2 ≤ n ≤ 10^4). The hidden permutation p is a list of integers from 0 to n-1. The function can ask up to 3n queries of the form "? a b c d" to compare bitwise OR results, and must eventually output a pair of indices "! i j" such that p_i ⊕ p_j is maximized. The sum of n over all test cases does not exceed 10^4.
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
        
    #State: The loop has completed its execution for all test cases. For each test case, `maxi` is the index of the element in the permutation `p` that, when XORed with the element at `mini`, gives the maximum possible value. `arr` contains the indices of elements that have the same maximum bitwise OR value with `maxi`. `mini` is the index of the element in `arr` that, when XORed with the element at `maxi`, gives the maximum possible value. `_` is the number of test cases, and `n` is the input integer for the last test case.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` (2 ≤ n ≤ 10^4). For each test case, it interacts with an environment that has a hidden permutation `p` of integers from 0 to n-1. The function queries the environment to find two indices `maxi` and `mini` such that the bitwise XOR of `p[maxi]` and `p[mini]` is maximized. After processing all test cases, the function outputs the pair of indices `maxi` and `mini` for each test case, ensuring that the maximum possible XOR value is achieved. The function does not return any value but prints the results directly.

