#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type initially possessed.
def func():
    ans_list = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        ans = a[0]
        
        res = n - 1
        
        for i in range(n - 1):
            dif = a[i + 1] - a[i]
            if dif == 0:
                res -= 1
            if dif != 0:
                if k >= dif * (i + 1):
                    ans += dif
                    k -= dif * (i + 1)
                    res -= 1
                else:
                    ans += k // (i + 1)
                    if i != 0:
                        res += k % (i + 1)
                    k = 0
                    break
                if k == 0:
                    break
        
        if k != 0:
            ans += k // n
            res += k % n
        
        ans += (ans - 1) * (n - 1)
        
        ans += res
        
        ans_list.append(ans)
        
    #State: Output State: The final output state after the loop executes all its iterations will contain a list `ans_list` where each element is calculated based on the given logic within the loop. Specifically, for each iteration, the variable `ans` is updated according to the differences between consecutive elements in the sorted list `a`, the value of `k`, and the size of the list `n`. After processing all elements in the input as specified by the loop, `ans_list` will contain the cumulative result of `ans` for each input set processed.
    #
    #To provide a more concrete example, let's assume we have processed `m` sets of inputs (where `m` is the total number of iterations the loop runs). For each set, the value of `ans` is updated based on the operations described in the loop, and then appended to `ans_list`. Therefore, `ans_list` will contain `m` elements, each representing the final value of `ans` for each respective input set.
    #
    #In natural language, the output state can be described as follows:
    #
    #Output State: `ans_list` is a list containing the final value of `ans` for each input set processed by the loop. Each element in `ans_list` represents the cumulative result after applying the specified operations on the input lists `a` for each set, with `k` and `n` being the key parameters influencing the final value of `ans`.
    for a in ans_list:
        print(a)
        
    #State: `ans_list` contains the final value of `ans` for each input set processed by the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it calculates a value `ans` based on the initial number of cards (`a`), the number of test cases (`t`), and the available extra cards (`k`). It sorts the list of card counts, iterates through the list to adjust `ans` based on the differences between consecutive card counts and the available extra cards. Finally, it appends each calculated `ans` to a list `ans_list` and prints the contents of `ans_list`.

