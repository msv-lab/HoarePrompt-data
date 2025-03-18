#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. The list of integers c represents the numbers written on the cards, where each c_i is an integer such that 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: t is an integer between 1 and 500, i is 997, n is an input integer, k is an input integer, l is a list of integers obtained from splitting the input string on spaces and converting each element to an integer, p is a list of counts where each element is the count of a unique element in l, and the loop has completed all its iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers t, n, k, and a list of integers c. It then calculates the count of each unique number in the list c and checks if the maximum count is greater than or equal to k. If true, it prints k - 1; otherwise, it prints n. The function does not return any value explicitly but prints the result for each test case.

