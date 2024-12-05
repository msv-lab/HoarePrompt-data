#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100000), f is a non-negative integer (0 ≤ f ≤ n), and each of the following n pairs of integers (k_i, l_i) represents the number of products (k_i) and the number of clients (l_i) on the i-th day, where 0 ≤ k_i, l_i ≤ 10^9.
def func():
    n, f = map(int, input().split())
    days = []
    for _ in range(n):
        k, l = map(int, input().split())
        
        days.append((k, l))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `f` is a non-negative integer (0 ≤ f ≤ n), `days` is a list containing `n` tuples (k, l) where each tuple is derived from the input, `k` and `l` are input integers corresponding to each iteration of the loop.
    days.sort(key=lambda x: x[1] - x[0], reverse=True)
    sold = 0
    for i in range(n):
        if i < f:
            sold += min(days[i][0] * 2, days[i][1])
        else:
            sold += min(days[i][0], days[i][1])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `f` is a non-negative integer, `days` is a list sorted in descending order based on the value of `l - k` for each tuple (k, l), `sold` is the total calculated from the first `f` elements using the formula `min(days[i][0] * 2, days[i][1])` and the remaining `n-f` elements using `min(days[i][0], days[i][1])`.
    print(sold)
#Overall this is what the function does:The function accepts a positive integer `n` and a non-negative integer `f`, followed by `n` pairs of integers representing the number of products and clients for each day. It calculates the total number of products sold based on the number of clients, prioritizing the first `f` days by allowing double the products to be sold if possible, while for the remaining days it sells based on the available products. The final total sold is printed. It handles up to 100,000 days and large integer values for products and clients, ensuring that the sorting and calculation of sold products respect the constraints provided.

