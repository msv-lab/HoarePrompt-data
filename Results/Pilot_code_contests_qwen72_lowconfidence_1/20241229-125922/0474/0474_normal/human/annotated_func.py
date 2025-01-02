#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and a list of integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 representing the heights of the children.
def func():
    n = int(raw_input())
    arr = [int(__) for __ in raw_input().split()]
    arr.sort(reverse=True)
    newl = list()
    fl = 0
    for el in arr:
        if fl == 0:
            newl.append(el)
            fl = 1
        else:
            newl = [el] + newl
            fl = 0
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 100), `arr` is a list of integers representing the heights of the children sorted in descending order with a length of `n`, `newl` is a list containing the elements of `arr` in an alternating order (first element of `arr` is the last in `newl`, second is the first in `newl`, and so on), `fl` is 0 if `n` is even and 1 if `n` is odd, `el` is the last element of `arr`.
    print(' '.join([str(x) for x in newl]))
#Overall this is what the function does:The function reads an integer `n` and a list of integers `arr` representing the heights of `n` children. It sorts `arr` in descending order and then rearranges the elements into a new list `newl` such that the elements are placed alternately (the first element of `arr` becomes the last in `newl`, the second becomes the first, and so on). Finally, it prints the elements of `newl` separated by spaces. The function does not return any value. The final state of the program includes `n` being an integer within the range 2 to 100, `arr` being a sorted list of integers in descending order, and `newl` containing the elements of `arr` in the specified alternating order. The variable `fl` is 0 if `n` is even and 1 if `n` is odd. The function does not compute or return the maximum height difference among the children as suggested by the incorrect annotation.

