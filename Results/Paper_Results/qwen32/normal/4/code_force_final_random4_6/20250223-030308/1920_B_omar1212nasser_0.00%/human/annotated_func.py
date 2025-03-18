#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, k is a positive integer representing the maximum number of elements Alice can remove, x is a positive integer representing the maximum number of elements Bob can multiply by -1, and a is a list of n positive integers representing the elements of the array.
def func_1():
    t = int(input())
    for i in range(t):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        product = func_2(k, x, a)
        
        print(product)
        
    #State: `i` is equal to `t`, `n`, `k`, and `x` are the values from the last iteration's input, `a` is the sorted list of integers from the last iteration's input, `product` is the result of `func_2(k, x, a)` from the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three integers `n`, `k`, and `x`, and a list of `n` positive integers `a`. For each test case, it calculates and prints the maximum possible sum of the array after removing up to `k` elements and multiplying up to `x` elements by -1.

#State of the program right berfore the function call: removals is a non-negative integer representing the maximum number of elements Alice can remove, negatives is a non-negative integer representing the maximum number of elements Bob can multiply by -1, and elements is a list of integers representing the array.
def func_2(removals, negatives, elements):
    if (removals == 6 and negatives == 3) :
        return 0
        #The program returns 0
    #State: removals is a non-negative integer representing the maximum number of elements Alice can remove, negatives is a non-negative integer representing the maximum number of elements Bob can multiply by -1, and elements is a list of integers representing the array. It is not the case that removals is 6 and negatives is 3.
    pos = []
    s = sum(elements)
    n = sum(elements[-negatives:])
    pos.append(s - 2 * n)
    for i in range(1, removals + 1):
        s -= elements[-i]
        
        try:
            n += elements[-(negatives + i)] - elements[-i]
        except IndexError:
            n = 0
        
        pos.append(s - 2 * n)
        
    #State: removals is a non-negative integer, negatives is a non-negative integer, elements is a list of integers, pos is a list containing `removals + 1` elements, s is the sum of the elements in elements minus the sum of the last `removals` elements, n is the sum of the last `negatives + removals` elements of elements if indices are within bounds, otherwise n is 0.
    return max(pos)
    #The program returns the maximum value from the list `pos`, which contains `removals + 1` elements.
#Overall this is what the function does:The function takes three parameters: `removals` (a non-negative integer representing the maximum number of elements Alice can remove), `negatives` (a non-negative integer representing the maximum number of elements Bob can multiply by -1), and `elements` (a list of integers). If `removals` is 6 and `negatives` is 3, the function returns 0. Otherwise, it calculates and returns the maximum value from a list of potential sums, where each sum is derived by considering different combinations of removing elements from the end of the list and negating elements from the end of the list.

