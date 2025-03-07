#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: Output State: The value of `score` is the sum of every second element in the list `l`, starting from the first element, and going up to the second-to-last element. Specifically, `score` will be the sum of elements at indices 0, 2, 4, ..., up to `2 * n - 2`. The variable `t` remains unchanged, `n` remains unchanged, and `l` remains the same sorted list of integers. The loop variable `i` will be equal to `2 * n - 1` after the loop completes.
    #
    #In simpler terms, after the loop has executed all its iterations, the `score` will be the sum of all elements in the list `l` that are at even indices (starting from index 0). The variable `t` stays the same, `n` remains unchanged, and `l` retains its sorted form. The loop variable `i` will be equal to `2 * n - 1` because it increments by 2 in each iteration, starting from 0 up to but not including `2 * n`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and a list of \( 2n \) integers. It then sorts the list and calculates the sum of every second element starting from the first element. Finally, it prints the calculated sum for each test case. The function does not return any value but prints the results directly.

