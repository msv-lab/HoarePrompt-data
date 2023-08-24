"""
To maximize the score, we want to perform transformations that result in the largest absolute value of x. 
Since we can only transform a into b (or b into a) if and only if a * x = b (or b * x = a), 
this means that we want to find the largest possible value of |x|.

For any number n > 2, there will always be a pair of integers (a, b) such that a * x = b or b * x = a, 
where x is not equal to 1 or -1. Specifically, if we choose a = n and b = n - 1, 
then the transformation will be n * x = n - 1. Solving for x, we get x = (n - 1) / n. 
Since x is not equal to 1 or -1, this means that the maximum possible value of |x| is (n - 1) / n.

To calculate the maximum score, we need to find all possible pairs of (a, b) and calculate the score for each pair.
Since there are n - 1 integers greater than 1 and less than or equal to n, 
there will be (n - 1) * (n - 1) = (n - 1)^2 possible pairs of (a, b). 
For each pair, the score will be |(n - 1) / n| = (n - 1) / n.

Therefore, the maximum score will be (n - 1) / n * (n - 1) ^ 2 = (n - 1) * (n - 1) = (n - 1) ^ 2.

Now we can implement the solution in Python.
"""

n = int(input())

if n == 2:
    print(0)
else:
    print((n - 1) ** 2)
    