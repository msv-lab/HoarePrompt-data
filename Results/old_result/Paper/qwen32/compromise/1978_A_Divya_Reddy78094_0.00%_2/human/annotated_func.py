#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 100) representing the number of books. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of pages in each book. The number of test cases t is given at the beginning and satisfies 1 ≤ t ≤ 500.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: For each test case, the sum of the two largest numbers from the list of pages is printed. The values of `t`, `n`, and `nums` are not retained after each iteration and are reinitialized in each loop iteration based on the input.
#Overall this is what the function does:For each test case, the function calculates and prints the sum of the two largest numbers from a list of integers representing the number of pages in books.

