#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of lists where each inner list contains n (1 ≤ n ≤ 2 · 10^5) non-negative integers a_1, ..., a_n (0 ≤ a_j < 2^31). The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = n
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if s in dic:
                dic[s] -= 1
                ans -= 1
                if dic[s] == 0:
                    del dic[s]
            elif i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            print(ans)
        
    #State: The loop will execute `times` iterations, and for each iteration, it will read `n` and `data` from the input, update the `dic` dictionary, and print the value of `ans`. After all iterations, the variables `t` and the list of lists containing the test cases will remain unchanged. The variables `times`, `check`, `n`, `data`, `dic`, and `ans` will be in their final states after the last iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, and for each test case, it reads an integer `n` and a list of `n` non-negative integers. It then processes each integer in the list, updating a dictionary `dic` and a variable `ans`. The function prints the value of `ans` after processing each integer in the list. After all test cases are processed, the function does not return any value, but the state of the program includes the final values of `times`, `check`, `n`, `data`, `dic`, and `ans` after the last iteration. The function does not modify the input `t` or the list of lists containing the test cases.

