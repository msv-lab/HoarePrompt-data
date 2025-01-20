# Read input
n = int(input())
a = list(map(int, input().split()))

# Check if there exists at least one '1' followed by a '0' in the list
if 0 in a and a[:a.index(0)].count(1) > 0:
    # It's possible to arrange brackets to make the expression false
    print("YES")
    result = []
    
    # Find the first 1 and the first 0 after that
    first_one_index = a.index(1)
    first_zero_index = a[first_one_index:].index(0) + first_one_index
    
    # Building the expression
    for i in range(first_one_index):
        result.append(str(a[i]) + "->")
    result.append("(")
    for i in range(first_one_index, first_zero_index):
        result.append(str(a[i]) + "->")
    result.append(str(a[first_zero_index]))
    result.append(")")
    for i in range(first_zero_index + 1, n):
        result.append("->" + str(a[i]))
    
    print("".join(result))
else:
    # It's not possible to make the expression false
    print("NO")
