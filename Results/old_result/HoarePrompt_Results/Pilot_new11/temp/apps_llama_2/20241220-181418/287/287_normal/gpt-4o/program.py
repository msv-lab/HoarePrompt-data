n = int(input())

# To find the number of different weights of its splits, we need to consider
# the number of ways we can divide n into parts such that the parts are non-increasing
# and the largest part (first element) appears a certain number of times.

# Let's denote k as the weight of the split. The smallest k is `1` (split is [n]),
# and the largest k is equal to n (split is [1, 1, ..., 1]).

# Thus, the number of different weights of its splits is equal to the number of
# divisors of n. This is because each divisor represents a possible "block size"
# where the largest number in the split repeats.

def count_divisors(num):
    count = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
        i += 1
    return count

print(count_divisors(n))
