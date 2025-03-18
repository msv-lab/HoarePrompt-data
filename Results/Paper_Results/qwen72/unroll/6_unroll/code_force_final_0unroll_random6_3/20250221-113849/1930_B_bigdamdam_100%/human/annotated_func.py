#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case is defined by a single integer n (3 ≤ n ≤ 10^5) representing the length of the permutation. The number of test cases t is a positive integer (1 ≤ t ≤ 10^3), and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: The function `func` will have processed all test cases, and for each test case, it will have printed a permutation of the integers from 1 to n, where n is the length of the permutation for that test case. The permutation is constructed such that the even-indexed positions (0, 2, 4, ...) are filled with the largest odd numbers in descending order, and the odd-indexed positions (1, 3, 5, ...) are filled with the smallest odd numbers in ascending order. The loop variable `i` in the outer loop will have completed all iterations from 0 to t-1, and the inner loop variables `i` and `ind` will have completed their respective iterations for each test case. The variable `p` will have been reset to a new permutation for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` (3 ≤ n ≤ 10^5) and prints a permutation of the integers from 1 to n. The permutation is constructed such that even-indexed positions (0, 2, 4, ...) are filled with the largest odd numbers in descending order, and odd-indexed positions (1, 3, 5, ...) are filled with the smallest odd numbers in ascending order. After processing all test cases, the function completes and the final state includes the printed permutations for each test case. The function does not return any value.

