#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the list of integers c represents the numbers written on the cards, where each c_i is an integer such that 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        
        arrC = list(map(int, input().split()))
        
        hashmap = {}
        
        ans = n
        
        for i in arrC:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] >= k:
                ans = k - 1
        
        print(ans)
        
        t -= 1
        
    #State: Output State: After the loop executes all the iterations, `t` will be `0`, `n` will be an integer from the last input split, `k` will be an integer from the last input split, `arrC` will be a list of integers from the last input split, and `ans` will be `k - 1` if any element in `arrC` appears at least `k` times; otherwise, `ans` will be `n`.
    #
    #This means that after the loop completes, `t` will have reached `0` because it is decremented by `1` in each iteration. The final values of `n`, `k`, and `arrC` will correspond to the inputs provided in the last iteration of the loop. The variable `ans` will hold the value `k - 1` if any element in `arrC` was found to appear `k` or more times during the processing of `arrC`. If no such element was found, `ans` will retain its original value `n`.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads integers n and k, followed by a list of integers c. It then counts the occurrences of each number in c. If any number appears at least k times, it sets ans to k - 1; otherwise, ans remains n. Finally, it prints the value of ans for each test case and decrements t until it reaches 0.

