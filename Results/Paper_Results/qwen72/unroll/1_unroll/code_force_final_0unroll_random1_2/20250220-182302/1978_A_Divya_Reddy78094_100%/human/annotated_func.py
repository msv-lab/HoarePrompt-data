#State of the program right berfore the function call: The function should take two parameters: an integer t (1 ≤ t ≤ 500) representing the number of test cases, and a list of lists, where each inner list contains n integers (2 ≤ n ≤ 100) representing the number of pages in each book for a test case. Each integer a_i in the inner lists should satisfy 1 ≤ a_i ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        print(max(nums[:-1]) + nums[-1])
        
    #State: The function will have printed the sum of the maximum of the first n-1 elements and the last element for each of the t test cases. The variables `t` and the list of lists containing the test cases remain unchanged.
#Overall this is what the function does:The function `func` takes no parameters and reads input from the user. It processes `t` test cases, where `t` is an integer provided by the user (1 ≤ t ≤ 500). For each test case, it reads an integer `n` (2 ≤ n ≤ 100) representing the number of books, and then reads a list of `n` integers where each integer represents the number of pages in a book (1 ≤ a_i ≤ 10^9). The function then prints the sum of the maximum of the first `n-1` elements and the last element for each test case. The function does not return any value. After the function concludes, the user will have seen the printed results for each test case, and the variables `t` and the list of lists containing the test cases remain unchanged.

