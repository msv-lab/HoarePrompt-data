#State of the program right berfore the function call: a, b, c, and d are integers such that 0 <= a, b, c, d < n, where n is the length of the permutation p.
def func_1(a, b, c, d):
    request = f'? {a} {b} {c} {d}'
    print(request, flush=True)
    #This is printed: Output:
    return input()
    #The program returns the value provided by the user input.
#Overall this is what the function does:The function accepts four integer parameters `a`, `b`, `c`, and `d`, each within the range from 0 to `n-1`, where `n` is the length of a permutation `p`. It prints a formatted string containing these parameters and then returns the value provided by the user input.

#State of the program right berfore the function call: n is a positive integer representing the length of the secret permutation p, where 2 <= n <= 10^4.
def func_2(n):
    max_item_idx = 0
    for i in range(1, n):
        ans = func_1(max_item_idx, max_item_idx, i, i)
        
        if ans == '<':
            max_item_idx = i
        
    #State: max_item_idx is the index of the maximum element in the permutation p.
    pair_idx = max_item_idx
    for i in range(n):
        ans1 = func_1(max_item_idx, pair_idx, max_item_idx, i)
        
        if ans1 == '<':
            pair_idx = i
        elif ans1 == '=':
            ans2 = func_1(pair_idx, pair_idx, i, i)
            if ans2 == '>':
                pair_idx = i
        
    #State: max_item_idx is the index of the maximum element in the permutation p; pair_idx is equal to max_item_idx.
    print(f'! {max_item_idx} {pair_idx}')
    #This is printed: ! [max_item_idx] [pair_idx] (where max_item_idx is the index of the maximum element in the permutation p and pair_idx is equal to max_item_idx)
#Overall this is what the function does:The function `func_2` accepts a parameter `n`, which is a positive integer representing the length of a secret permutation `p`. It determines the index of the maximum element in the permutation and prints this index twice, indicating the position of the maximum element in the permutation.

