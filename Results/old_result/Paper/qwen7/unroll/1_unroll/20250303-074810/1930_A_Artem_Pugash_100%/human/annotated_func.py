#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, and for each test case, n is an integer such that 1 ≤ n ≤ 50, and the numbers written on the whiteboard are 2n integers a_1, a_2, …, a_{2n} where 1 ≤ a_i ≤ 10^7. After executing the loop, the score is calculated as the sum of every first element in each pair of sorted elements from the input list.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( n \) and \( 2n \) integers \( a_1, a_2, \ldots, a_{2n} \). For each test case, it sorts the \( 2n \) integers and calculates the score as the sum of the first element of each consecutive pair of elements in the sorted list. The function prints the score for each test case and does not return any value.

