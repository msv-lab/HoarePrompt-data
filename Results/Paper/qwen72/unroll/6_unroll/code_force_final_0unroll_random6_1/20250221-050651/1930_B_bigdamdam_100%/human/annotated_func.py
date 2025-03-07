#State of the program right berfore the function call: The function is designed to handle multiple test cases, where each test case involves a single integer n (3 ≤ n ≤ 10^5) representing the length of the permutation. The total number of test cases t is a positive integer (1 ≤ t ≤ 10^3), and the sum of all n values across test cases does not exceed 10^5.
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
        
    #State: The function will have processed all test cases, and for each test case, it will have generated and printed a permutation of length n, where the permutation alternates between the largest and smallest remaining numbers, starting with the largest. The variables `i` and `ind` will have their final values after the last iteration of the loop, but these values are not significant as they are local to the loop. The total number of test cases `t` will remain unchanged, and the sum of all `n` values across test cases will also remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` (3 ≤ n ≤ 10^5) representing the length of a permutation. For each test case, it generates and prints a permutation of length `n` where the permutation alternates between the largest and smallest remaining numbers, starting with the largest. After processing all test cases, the function has no return value, but it has printed the required permutations for each test case. The total number of test cases `t` and the sum of all `n` values across test cases remain unchanged.

