#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 1 ≤ n ≤ 50, and a is a list of 2n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: t is an integer such that 1 ≤ t ≤ 5000, and the loop has executed exactly t times. For each of the t test cases, n is an input integer, l is a sorted list of integers derived from the corresponding input, and score is the sum of elements at even indices from 0 to 2*(n-1) in the list l. The final output consists of t scores, one per line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `2n` integers. It sorts the list and calculates the sum of the elements at even indices (0, 2, 4, ..., 2n-2). It then prints this sum for each test case.

