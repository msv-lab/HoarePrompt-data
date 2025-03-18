# AUTHOR @perf3ct aka @hjacobs3
# ez ez ez
 
 
def solve(array, find):
    # print('target', find)
    n = len(array)
    # new_array = [i for i in range(1, n + 1)]
    # print(array)
    l, r = 0, n - 1
    while l <= r:
        # pr('dog')
        mid = (l + r) // 2
        if array[mid] >= find:
            r = mid - 1
        else:
            l = mid + 1
    if l != array.index(find):
        print(1)
        return [str(l+1), str(array.index(find)+1)]
    else:
        print(0)
 
 
# Read the number of test cases
t = int(input())
 
# Process each test case
while t > 0:
    # Read input for the test case, for example, an integer
    n, x = map(int, input().split(" "))
 
    array = [int(v) for v in input().split(" ")]
    
    # Process the test case
    
    # Example: Print the read integer
    res = solve(array, x)
    if res:
        print(" ".join(res))
    
    # Move to the next test case
    t -= 1