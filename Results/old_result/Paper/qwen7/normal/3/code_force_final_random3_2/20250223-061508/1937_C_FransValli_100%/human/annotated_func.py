#State of the program right berfore the function call: This is an interactive problem where you need to find two indices i and j such that \( p_i \oplus p_j \) is maximized for a given permutation \( p_0, p_1, \ldots, p_{n-1} \) of \(\{0,1,\ldots,n-1\}\). You can ask up to 3n queries of the form "? a b c d" to compare the results of bitwise OR operations on pairs of elements in the permutation. After finding the indices, you must print "! i j".
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
        
    #State: Output State: mini is equal to n-1, arr is an empty list, maxi is equal to n-1, and the loop has executed for all iterations of n.
    #
    #Explanation: After the loop completes all its iterations, the value of `maxi` will be set to `n-1` because it is updated to the largest index during each iteration. The variable `mini` will also end up being `n-1` as it is updated to the smallest index within the array `arr` in each iteration. By the end of the loop, `arr` will be an empty list because all possible indices have been checked and added to `arr`, then replaced with a new minimum value in subsequent iterations. The loop has processed all iterations of `n`, meaning it has gone through all indices from 1 to `n-1`.
#Overall this is what the function does:The function interacts with an external permutation of numbers from 0 to n-1. It makes up to 3n queries comparing bitwise OR operations on pairs of elements in the permutation. After identifying the indices i and j that maximize the bitwise XOR operation \( p_i \oplus p_j \), it prints the result as "! i j".

