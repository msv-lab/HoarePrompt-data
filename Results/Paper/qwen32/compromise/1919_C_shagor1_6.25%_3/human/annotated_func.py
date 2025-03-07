#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: t test cases have been processed, each with an integer n and a list of integers a. For each test case, x is the smallest element in a, y is the second smallest unique element in a (or the same as x if all elements are the same), and ans is the count of elements in a that are greater than both x and y.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the number of elements in the list that are greater than both the smallest and the second smallest unique elements in the list.

