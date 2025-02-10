#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 represents the number of pages in each book.
def func():
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        
        ls = input().split()
        
        last = int(ls.pop())
        
        other = int(sorted(ls).pop())
        
        print(last + other)
        
    #State: Output State: `t` must be greater than 2, `i` is the final iteration count minus one, `n` is an integer input stripped of leading/trailing whitespace, `ls` is a list of strings with elements continuously removed based on the loop iterations, `last` is the last element of the updated `ls` converted to an integer, `other` is the second largest element in the sorted list `ls`.
    #
    #In simpler terms, after the loop has executed all its iterations:
    #- The variable `t` will be the total number of iterations the loop ran, which must be greater than 2.
    #- The variable `i` will be the last iteration index, which is `t - 1`.
    #- The variable `n` will be the last integer input provided during any of the iterations.
    #- The variable `ls` will be a list of strings, with elements being removed in each iteration based on the input provided.
    #- The variable `last` will be the last remaining element in the list `ls`, converted to an integer.
    #- The variable `other` will be the second largest element in the sorted version of the list `ls`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) indicating the number of books, followed by another integer \( n \) and a list of \( n \) integers representing the number of pages in each book. For each test case, it removes the last and the second largest page counts from the list, sums them, and prints the result. After processing all test cases, it outputs the sum of the last and second largest page counts for each case.

