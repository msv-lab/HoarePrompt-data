"""
To solve this problem, we can use a dynamic programming approach.
Let's define a function E(n) that represents the expected total number of gifts taken out of the bag for a family of size n.
We can observe that:
- If there are only 2 people in the family, the expected number of gifts taken out is 3. This is because there are only 2 possible orderings: (1, 2) and (2, 1). In both cases, the last person will always get their own gift, so we need to restart the process and take 3 gifts out of the bag.
- For larger families, we can consider the last person in the family (person n). There are n-1 other people who can potentially pick person n's gift. The probability of this happening is (n-1)/n. In this case, we will need to restart the process and take E(n) gifts out of the bag. However, there is also a 1/n chance that person n's gift will be picked by someone else. In this case, person n will not need to restart the process and will just need to pick their gift from the remaining n-1 gifts. 
Therefore, we can write the following recurrence relation:
E(n) = (n-1)/n * (E(n) + 1) + 1/n * (E(n-1) + 1)
Simplifying the equation, we get:
E(n) = n/(n-1) * E(n-1) + 1
We can calculate E(n) iteratively for n = 2 to n using this formula. The base case is E(2) = 3.
"""
n = int(input())

# Calculate the expected total number of gifts taken out for a family of size n
def calculate_expected_total_gifts(n):
    if n == 2:
        return 3.0
    
    # Initialize variables
    E = [0.0] * (n + 1)
    E[2] = 3.0
    
    # Calculate E(n) iteratively for n = 3 to n
    for i in range(3, n + 1):
        E[i] = i / (i - 1) * E[i - 1] + 1.0
    
    return E[n]

# Print the result with 9 decimal places precision
print(format(calculate_expected_total_gifts(n), '.9f'))