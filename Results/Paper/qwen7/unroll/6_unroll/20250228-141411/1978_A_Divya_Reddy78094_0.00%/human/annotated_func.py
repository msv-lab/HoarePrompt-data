#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        nums = list(map(int, input().split()))
        
        nums.sort(reverse=True)
        
        print(nums[0] + nums[1])
        
    #State: The sum of the two largest numbers provided in each iteration, for a total of t iterations.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer t indicating the number of books and another integer n indicating the number of pages in each book. For each test case, it sorts the list of page counts in descending order and prints the sum of the two largest page counts. After processing all test cases, it does not return any value.

