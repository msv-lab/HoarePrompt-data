#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: After all iterations of the loop, `x` will be less than or equal to 0; `a` and `b` will contain the last integer inputs provided during the loop's final iteration; `rev[b]` will contain all integers `a` that were inputs along with `b` throughout the loop's iterations; `lst[a]` will contain all integers `b` that were inputs along with `a` throughout the loop's iterations.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: Output State: `one` is True, `lst[z]` is an empty list, `tmp` is now equal to the last element of `lst[tmp] - 2`, `x` will be less than or equal to 0 after all iterations, `a` will be the last integer input provided during the loop's final iteration, `b` will be the last integer input provided during the loop's final iteration, `rev[b]` will contain all integers `a` that were inputs along with `b` throughout the loop's iterations, `lst[a]` will contain all integers `b` that were inputs along with `a` throughout the loop's iterations.
    #
    #Explanation: After the loop has executed all its iterations, the condition `lst[tmp] != []` will eventually become false, causing the loop to terminate. Since the loop runs until `lst[tmp]` becomes empty, and given the pattern observed from the first three iterations, the final value of `tmp` will be the third last element of `lst[tmp]`. The variable `one` alternates between True and False with each iteration, so after an odd number of iterations (which we can assume is the case if it ran to completion), `one` will be True. All other variables (`x`, `a`, `b`, `rev`, and `lst`) will retain their final states from the last iteration of the loop.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: Output State: `one` is True, `two` is False, `tmp` is the last element of `rev[tmp]` after all elements have been popped from `rev[tmp]`.
    #
    #In natural language: After all iterations of the loop have finished, the variable `one` remains True because it was never changed to False within the loop. The variable `two` becomes False, as it alternates between True and False with each iteration, and since the loop runs an odd number of times (at least 3), `two` ends up being False. The variable `tmp` will be set to the last remaining element in the list `rev[tmp]` after all elements have been popped from it during the loop iterations.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function reads input values to construct a graph represented by adjacency lists and their reverses. It then checks two conditions involving traversals through the graph and prints 'Ron' if both conditions are met, otherwise it prints 'Hermione'. The function does not return any value but outputs the result based on the graph traversal outcomes.

