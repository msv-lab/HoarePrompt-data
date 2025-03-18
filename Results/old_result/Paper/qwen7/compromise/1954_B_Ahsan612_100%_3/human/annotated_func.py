#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 \cdot 10^5, and the array a is a list of n integers where 1 ≤ a_i ≤ n and the array a is beautiful. The sum of n over all test cases does not exceed 3 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: Postcondition: `same` is the minimum count of consecutive occurrences of any number in the list `ar` throughout the entire list, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is the final input integer after all iterations, `ar` is the final list of integers obtained from the input split and mapped to integers, `num` is the current number being tracked, `minn` is the minimum value of `same` found during the loop's execution, and `i` is equal to `len(ar) + 1`, indicating the loop has completed all iterations and moved past the last index of the list. `minn` is the smallest value of `same` found during the loop, and it is either equal to infinity or the length of the list `ar` in the if part, or `minn` is neither infinity nor the length of the list `ar` in the else part.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer n and a list of n integers. It then finds the minimum count of consecutive occurrences of any number in the list. If such a minimum count exists and is less than the length of the list, it prints this minimum count; otherwise, it prints -1. The function implicitly accepts the number of test cases and the inputs for each test case through standard input and does not return any value explicitly.

