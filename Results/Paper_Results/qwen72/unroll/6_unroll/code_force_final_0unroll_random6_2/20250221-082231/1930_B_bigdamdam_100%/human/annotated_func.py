#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case contains a single integer n (3 ≤ n ≤ 10^5) — the length of the permutation p. The sum of n over all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: The function `func` will print the permutations for each test case, where each permutation is a sequence of integers from 1 to n rearranged such that the even indices (0-based) contain the largest even numbers in descending order, and the odd indices contain the smallest odd numbers in ascending order. The loop will have completed all iterations, and the variables `i` and `n` will be in their final states after the last test case. The list `p` will be the last permutation generated, and `ind` will be the last value used for filling the permutation. The initial state of the function and the structure of the loop remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an integer `n` (3 ≤ n ≤ 10^5) representing the length of a permutation `p`. For each test case, it generates and prints a permutation of integers from 1 to `n` such that even indices (0-based) contain the largest even numbers in descending order, and odd indices contain the smallest odd numbers in ascending order. After processing all test cases, the function completes and the final state includes the last permutation `p` generated and the last value of `ind` used for filling the permutation. The function does not return any value.

