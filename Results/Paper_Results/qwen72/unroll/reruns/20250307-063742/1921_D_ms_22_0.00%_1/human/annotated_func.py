#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            n, m = map(int, input().split())
            
            a = list(map(int, input().split()))
            
            b = list(map(int, input().split()))
            
            b.sort()
            
            max_heap = []
            
            tp1 = 0
            
            tp2 = m - 1
            
            ans = 0
            
            for i in a:
                diff1 = abs(i - b[0])
                diff2 = abs(i - b[m - 1])
                if diff1 > diff2:
                    heapq.heappush(max_heap, (-diff1, i, 0))
                else:
                    heapq.heappush(max_heap, (-diff2, i, m - 1))
            
            while max_heap:
                item = heapq.heappop(max_heap)
                if item[2] < tp1 or item[2] > tp2:
                    diff1 = abs(item[1] - b[tp1])
                    diff2 = abs(item[1] - b[tp2])
                    if diff1 > diff2:
                        tp1 += 1
                        ans += diff1
                    else:
                        tp2 -= 1
                        ans += diff2
                else:
                    ans += -item[0]
                    if item[2] == tp1:
                        tp1 += 1
                    else:
                        tp2 -= 1
            
            print(ans)
            
        #State: t is 0, and the program has printed the sum of the maximum absolute differences for each test case.
    #State: *t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and m are integers where 1 ≤ n ≤ m ≤ 2 · 10^5, a_i is a list of n integers where 1 ≤ a_i ≤ 10^9, and b_i is a list of m integers where 1 ≤ b_i ≤ 10^9. The sum of m over all test cases does not exceed 2 · 10^5. If the program is executed as the main module, the program prints the sum of the maximum absolute differences for each test case. If the program is not executed as the main module, there is no change to the variables or output.
#Overall this is what the function does:The function `func` is designed to be executed as the main module. It processes a series of test cases, each defined by two integers `n` and `m`, a list of `n` integers `a_i`, and a list of `m` integers `b_i`. For each test case, it calculates the sum of the maximum absolute differences between each element in `a_i` and the closest elements in the sorted list `b_i`. The final state of the program is that `t` is 0, and the sum of these maximum absolute differences for each test case has been printed to the console. If the function is not executed as the main module, it does not perform any actions and leaves the variables and output unchanged.

