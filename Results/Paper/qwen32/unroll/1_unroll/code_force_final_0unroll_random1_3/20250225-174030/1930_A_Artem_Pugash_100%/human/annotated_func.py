#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 5000) representing the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 50), indicating that there are 2n integers on the whiteboard. The second line contains 2n integers a_1, a_2, ..., a_{2n} (1 ≤ a_i ≤ 10^7), which are the numbers written on the whiteboard.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: For each test case, the sum of every second element from the sorted list of 2n integers.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `2n` integers. For each test case, it calculates the sum of every second element from the sorted list of these integers and prints the result.

