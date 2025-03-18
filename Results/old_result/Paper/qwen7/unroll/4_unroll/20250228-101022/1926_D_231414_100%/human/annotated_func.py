#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5; the list of integers a_1, \ldots, a_n consists of non-negative integers less than 2^{31}; the sum of all n across all test cases does not exceed 2 \cdot 10^5.
def func():
    times = int(input())
    check = 2 ** 31 - 1
    for _ in range(times):
        n = int(input())
        
        data = list(map(int, input().split()))
        
        dic = dict()
        
        ans = 0
        
        check = 2 ** 31 - 1
        
        for i in data:
            s = i ^ check
            if i in dic:
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
            else:
                if s not in dic:
                    dic[s] = 0
                dic[s] += 1
                ans += 1
        
        print(ans)
        
    #State: Output State: `t` remains a positive integer such that 1 ≤ t ≤ 10^4; `check` remains 2147483647. After executing the loop, `ans` is the sum of the number of times each element and its XOR with `check` appeared an odd number of times across all inputs.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer \( t \) (number of test cases), an integer \( n \) (size of the list), and a list of \( n \) non-negative integers. It then calculates and prints the sum of the number of times each element and its XOR with \( 2^{31} - 1 \) appeared an odd number of times across all inputs. The function does not return any value but prints the result for each test case.

