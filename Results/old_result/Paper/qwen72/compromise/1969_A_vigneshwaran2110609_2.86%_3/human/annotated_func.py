#State of the program right berfore the function call: The function should be called within a loop that processes multiple test cases, where each test case consists of an integer n (2 ≤ n ≤ 50) representing the number of friends, and a list of integers p of length n (1 ≤ p_i ≤ n, p_i ≠ i, all p_i are distinct) representing the best friends of each friend.
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop has processed `n` test cases. For each test case, `x` is an input integer, `l` is a list of integers provided by the user, and `i` is `x - 1`. For each test case, if the loop finds any index `i` such that `l[l[i] - 1] == l[i] - 1`, then `flag` is set to True and the loop prints 2. If no such index is found, the loop completes all iterations, and `flag` remains unchanged, printing 3.
#Overall this is what the function does:The function `func` processes `n` test cases, where `n` is an integer input. For each test case, it reads an integer `x` and a list `l` of integers. It then checks if there exists any index `i` in the list `l` such that `l[l[i] - 1] == l[i] - 1`. If such an index is found, the function prints 2. If no such index is found, the function prints 3. The function does not return any value. After processing all `n` test cases, the program state is such that `n` test cases have been processed, and for each test case, either 2 or 3 has been printed based on the condition.

