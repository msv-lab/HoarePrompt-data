#State of the program right berfore the function call: The function operates in an interactive environment where it can make queries to find the maximum XOR of any two indices in a permutation of {0, 1, ..., n-1}. The input n is an integer such that 2 ≤ n ≤ 10^4, and the function can make at most 3n queries. The permutation p is fixed and not adaptive, and the function must output the indices i and j (0 ≤ i, j < n) that maximize p_i ⊕ p_j.
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
        
    #State: The loop has executed `int(input())` times, and for each execution, the final state is as follows:
#Overall this is what the function does:The function operates in an interactive environment to find and print the indices `i` and `j` (0 ≤ i, j < n) that maximize the XOR value `p_i ⊕ p_j` for a fixed permutation `p` of the set {0, 1, ..., n-1}. It does this for each test case specified by the user input. The function does not return any values; it only prints the results. After the function concludes, the interactive environment has received the maximum XOR indices for each test case.

