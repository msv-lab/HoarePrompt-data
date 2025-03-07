#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5000, n is an input integer such that 2 ≤ n ≤ 50, and p is a list of n integers where 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct. After executing the loop, the output consists of either '2' or '3' printed for each iteration based on the condition inside the inner loop.
    #
    #In more detail, for each iteration of the outer loop (i.e., for each element in the list `p`), the code reads two lines of input: an integer `x` and a list `l` of integers. It then checks if any element `l[l[i] - 1]` equals `l[i] - 1`. If such an element exists, it prints '2' and breaks out of the inner loop. Otherwise, it prints '3'. The final output state remains unchanged in terms of the values of `t`, `n`, and `p`, but the output will contain a series of '2's and '3's corresponding to the results of the loop's conditions.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` (2 ≤ n ≤ 50), and a list `p` of `n` distinct integers where each integer is between 1 and `n` and does not equal its index. For each test case, it reads an integer `x` and a list `l` of integers. It then checks if any element `l[l[i] - 1]` equals `l[i] - 1`. If such an element exists, it prints '2' and breaks out of the inner loop. If no such element is found, it prints '3'. The function does not return any value but outputs a series of '2's and '3's corresponding to the results of the loop's conditions for each test case.

