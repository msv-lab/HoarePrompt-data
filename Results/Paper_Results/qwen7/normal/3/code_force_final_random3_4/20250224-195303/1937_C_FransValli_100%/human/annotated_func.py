#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, based on the problem description, the interaction involves querying indices and comparing bitwise OR results to deduce the maximum XOR pair. The input consists of multiple test cases, each with a permutation of integers from 0 to n-1, and the interaction rules are specified for querying and answering.
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
        
    #State: `mini` is the smallest integer from 0 to `n-1`, `maxi` is `n-1`, `i` is `n`, `arr` contains all integers from 0 to `n-1`, and `res` is an input string which is either '<' or '='.
#Overall this is what the function does:The function interacts with an external system to process multiple test cases, each involving a permutation of integers from 0 to n-1. For each test case, it queries indices and compares bitwise OR results to determine the maximum and minimum values that form the maximum XOR pair. Finally, it outputs the result for each test case, consisting of the maximum and minimum values that yield the highest XOR result.

