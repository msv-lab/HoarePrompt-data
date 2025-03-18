#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the second line of each test case contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: Output State: The final value of `score` will be the sum of every second element in the list `l`, starting from the first element, up to the 2*n-1th index if `n` is within the bounds of the list length. After all iterations, the list `l` remains a sorted list of integers entered by the user, and `n` is the integer input that determines the number of pairs of elements to sum. The variable `i` will be equal to `2 * n` after the loop finishes.
    #
    #In simpler terms, the final `score` will be the sum of all elements in `l` that are at even indices (0, 2, 4, ..., 2*n-2), provided that `n` is large enough to ensure at least `len(l)//2` iterations. If `n` is smaller than necessary, the loop will terminate early, but the final `score` will still be the sum of the even-indexed elements up to the point where the loop completes.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and \( 2n \) integers. It then sorts these integers and calculates the sum of every second element starting from the first element. The function prints this sum for each test case and leaves the sorted list and the value of \( n \) unchanged after processing.

