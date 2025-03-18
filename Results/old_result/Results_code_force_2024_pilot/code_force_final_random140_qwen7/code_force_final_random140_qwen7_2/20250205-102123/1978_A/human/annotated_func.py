#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: t is an integer greater than 2, i is 997, n is the integer input split from the input string, ls is a list of strings without the last element, last is the last element of the original ls converted to an integer, other is the second largest element in the original list ls converted to an integer and sorted, then popped.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( t \) (number of test cases), an integer \( n \) (number of books), and a list of \( n \) integers representing the number of pages in each book. For each test case, it calculates and prints the sum of the largest and second-largest page counts.

