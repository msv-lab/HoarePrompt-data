#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers a_1, a_2, ..., a_{2n} are positive integers such that 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers a_1, a_2, ..., a_{2n} are positive integers such that 1 ≤ a_i ≤ 10^7. After executing the loop, the score is calculated as the sum of the first and third, fifth, etc., elements in the sorted list l for each test case, and printed for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n`, followed by a list of `2n` positive integers. It then sorts this list and calculates the sum of every other element starting from the first element. This sum is referred to as the score. Finally, the function prints the score for each test case.

