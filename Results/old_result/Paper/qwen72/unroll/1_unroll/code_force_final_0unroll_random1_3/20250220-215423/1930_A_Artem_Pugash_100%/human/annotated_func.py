#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 5000) representing the number of test cases, and a list of lists, where each inner list contains 2n integers (1 ≤ n ≤ 50 and 1 ≤ a_i ≤ 10^7) for the numbers written on the whiteboard.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = sorted(list(map(int, input().split())))
        
        score = 0
        
        for i in range(0, 2 * n, 2):
            score += l[i]
        
        print(score)
        
    #State: The function will print the sum of the smaller numbers in each pair of the sorted list for each test case. The variables `t` and the list of lists will remain unchanged. The variable `score` will be reset to 0 for each test case.
#Overall this is what the function does:The function `func` reads input from the user to process multiple test cases. For each test case, it reads an integer `n` and a list of 2n integers, sorts the list, and calculates the sum of the smaller numbers in each pair of the sorted list. The function prints the sum for each test case. The function does not return any value, and the input variables `t` and the list of lists are not modified.

