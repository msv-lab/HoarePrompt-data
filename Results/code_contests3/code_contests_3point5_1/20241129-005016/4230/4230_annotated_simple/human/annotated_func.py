#State of the program right berfore the function call: **
def func():
    n = map(int, raw_input().split())
    n = n[0]
    c = map(int, raw_input().split())
    ans = 0
    for i in range(n - 2, -1, -1):
        if c[i] != c[i + 1]:
            ans = i + 1
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 2, `c` is a list of integers, `ans` is updated to the value of the last index of `c` + 1 where the element at that index is different from the previous element, `i` is either -1 or 0 depending on the last iteration, and the loop has checked for consecutive elements in the list `c` until finding a pair that is different from each other.
    print(ans)
#Overall this is what the function does:The function reads input from the user, processes the input to find the index of the last element in the list that is different from its previous element, and then prints out this index. The function does not accept any parameters and does not have a specific return value.

