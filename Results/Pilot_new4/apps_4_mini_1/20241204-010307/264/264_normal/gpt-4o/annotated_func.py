#State of the program right berfore the function call: n is an integer between 1 and 100 (inclusive), m is an integer between 1 and 10,000 (inclusive), and a_i is an integer between 1 and 100 (inclusive) for each i from 1 to n.
def func():
    n = int(input())
    m = int(input())
    a = [int(input()) for _ in range(n)]
    initial_max = max(a)
    total_people = sum(a)
    max_k = initial_max + m
    min_k = (total_people + m + n - 1) // n
    print(min_k, max_k)
#Overall this is what the function does:The function accepts two inputs, `n` and `m`, where `n` is the number of elements in an array and `m` is an additional integer value. It then reads `n` integers into an array `a`. The function calculates the maximum value of the array `a` and the total of all elements in `a`. It computes two values: `min_k`, which is the smallest integer greater than or equal to the average of the total people plus `m`, and `max_k`, which adds `m` to the maximum value in the array. Finally, it prints both `min_k` and `max_k`. The function does not have any explicit return values; it simply outputs the calculated values to the console.

