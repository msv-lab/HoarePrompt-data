#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where each p_i is an integer such that 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: Output State: The loop will execute all its iterations, and since the condition `j == 0` is met after the third iteration, the loop will print `3` and terminate. Therefore, `i` will be equal to `n`, `t` is an integer such that 1 ≤ t ≤ 5000, `n` is the input integer, `l` is a list of integers obtained from splitting the final input string and converting each element to an integer, `j` is 0, `p` is the integer at index `n-1` of the list `l`, `q` is the integer at index `p - 1` of the list `l`. After the loop completes, the program will print `3` and end.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \), a list of \( n \) distinct integers \( p \), and checks if the sequence described by \( p \) meets a specific condition. If the condition is met within the first two iterations of a loop, it prints `2`. Otherwise, after checking all elements, it prints `3`. The function does not return any value but prints the result for each test case.

