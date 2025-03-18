#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem description implies that the function should interact with an external entity to perform queries and receive responses. The interaction involves querying indices a, b, c, and d to compare bitwise OR results and finding indices i and j with maximum bitwise XOR.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        maxi = 0
        
        for i in range(1, n):
            print('?', maxi, maxi, i, i, flush=True)
            res = input()
            if res == '<':
                maxi = i
        
        arr = [0]
        
        for i in range(1, n):
            print('?', maxi, arr[0], maxi, i, flush=True)
            res = input()
            if res == '<':
                arr = [i]
            elif res == '=':
                arr.append(i)
        
        mini = arr[0]
        
        for item in arr[1:]:
            print('?', mini, mini, item, item, flush=True)
            res = input()
            if res == '>':
                mini = item
        
        print('!', maxi, mini, flush=True)
        
    #State: Output State: The output state will consist of two integers, `maxi` and `mini`, which are determined by the comparisons made within the loop. Specifically, `maxi` is the index with the maximum result from bitwise XOR comparisons, and `mini` is the index among those with the minimum result from bitwise OR comparisons relative to `maxi`. The exact values of `maxi` and `mini` depend on the input provided during the execution of the loop.
#Overall this is what the function does:The function interacts with an external entity to perform queries on indices. It first identifies an index `maxi` with the maximum bitwise XOR result. Then, it determines an index `mini` among those with the minimum bitwise OR result relative to `maxi`. Finally, it outputs the indices `maxi` and `mini`.

