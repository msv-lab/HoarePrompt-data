#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are positive integers such that 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 10^9 for all i.
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
            
        #State: Output State: `t` is 0, `n` and `m` are the integers entered in the last iteration, `a` is a list of integers obtained from the input in the last iteration and converted to integers, `b` is a list of integers sorted in ascending order obtained from the input in the last iteration and converted to integers, `max_heap` is an empty list, `tp1` is equal to `m - 1`, `tp2` is equal to 0, and `ans` is the cumulative sum of the differences calculated during all iterations of the loop as described.
        #
        #After all iterations of the loop have been executed, `t` will be 0 because the loop decrements `t` by 1 in each iteration until it reaches 0. The variables `n` and `m` will retain the values they had in the last iteration of the loop. Similarly, `a` and `b` will contain the lists of integers from the last iteration's inputs. The `max_heap` will be empty since it is cleared during each iteration. The variables `tp1` and `tp2` will be set to their boundary values (`m - 1` and 0) and will not change further. Finally, `ans` will hold the total sum of the differences calculated over all iterations of the loop.
    #State: `t` is 0, `n` and `m` are the integers entered in the last iteration, `a` is a list of integers obtained from the input in the last iteration and converted to integers, `b` is a list of integers sorted in ascending order obtained from the input in the last iteration and converted to integers, `max_heap` is an empty list, `tp1` is equal to `m - 1`, `tp2` is equal to 0, and `ans` is the cumulative sum of the differences calculated during all iterations of the loop as described.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers t, n, m, a_i, and b_i. It then calculates the minimum total difference between elements of array a and elements of array b by strategically pairing elements from b with those from a. The function returns the cumulative sum of these minimum differences for all test cases.

