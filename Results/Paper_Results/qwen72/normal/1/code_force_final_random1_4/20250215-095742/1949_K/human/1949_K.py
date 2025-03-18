# You are given n positive integers x1,x2,…,xn and three positive integers na,nb,nc satisfying na+nb+nc=n
#
# .
#
# You want to split the n
#
# positive integers into three groups, so that:
#
#     The first group contains na
#
# numbers, the second group contains nb numbers, the third group contains nc
# numbers.
# Let sa
# be the sum of the numbers in the first group, sb be the sum in the second group, and sc be the sum in the third group. Then sa,sb,sc
#
#     are the sides of a triangle with positive area.
#
# Determine if this is possible. If this is possible, find one way to do so.
# Input
#
# Each test contains multiple test cases. The first line contains an integer t
# (1≤t≤100000) — the number of test cases. The descriptions of the t
#
# test cases follow.
#
# The first line of each test case contains the integers n,na,nb,nc
# (3≤n≤200000,1≤na,nb,nc≤n−2,na+nb+nc=n
#
# ) — the number of integers to split into three groups, and the desired sizes of the three groups.
#
# The second line of each test case contains n
# integers x1,x2,…,xn (1≤xi≤109
#
# ).
#
# It is guaranteed that the sum of n
# over all test cases does not exceed 200000
#
# .
# Output
#
# For each test case, print YES
# if it is possible to split the numbers into three groups satisfying all the conditions. Otherwise, print NO
#
# .
#
# If such a split exists, then describe the three groups as follows.
#
# On the next line, print na
# integers a1,a2,…,ana
#
#  — the numbers in the first group.
#
# On the next line, print nb
# integers b1,b2,…,bnb
#
#  — the numbers in the second group.
#
# On the next line, print nc
# integers c1,c2,…,cnc
#
#  — the numbers in the third group.
#
# These na+nb+nc=n
# integers should be a permutation of x1,x2,…,xn
#
# , and they should satisfy the conditions from the statement.
#
# If there are multiple solutions, print any of them.
def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
 
def solve(n, na, nb, nc, numbers):
    # Sort the numbers in descending order for optimal distribution
    numbers.sort(reverse=True)
    # Prepare the groups and their sum trackers
    group_a, group_b, group_c = [], [], []
    sum_a, sum_b, sum_c = 0, 0, 0
 
    # Function to distribute a number to the group with the smallest sum or size constraint
    def distribute_number(num):
        nonlocal sum_a, sum_b, sum_c
        # Prioritize filling smaller groups to ensure size requirements are met
        if len(group_a) < na or (len(group_a) == na and sum_a <= min(sum_b, sum_c)):
            group_a.append(num)
            sum_a += num
        elif len(group_b) < nb or (len(group_b) == nb and sum_b <= min(sum_a, sum_c)):
            group_b.append(num)
            sum_b += num
        else:
            group_c.append(num)
            sum_c += num
 
    # Distribute numbers
    for num in numbers:
        distribute_number(num)
 
    # Check if the final groups form a valid triangle
    if can_form_triangle(sum_a, sum_b, sum_c):
        return "YES", group_a, group_b, group_c
    else:
        return "NO"
 
 
t = int(input())
out = []
for _ in range(t):
    n, na, nb, nc = map(int, input().split())
    x = list(map(int, input().split()))
    result = solve(n, na, nb, nc, x)  # Get the result directly
    if result == "NO":
        out.append("NO")  # Append "NO" directly if not possible
    else:
        # If possible, append a structured result that includes "YES" and the groups
        out.append(["YES", result[1], result[2], result[3]])  # Adjust according to your solve function's return structure
 
for result in out:
    if result == "NO":
        print(result)
    else:
        print(result[0])  # This prints "YES"
        for group in result[1:]:  # Iterate through the groups for printing
            print(" ".join(map(str, group)))