def find_mex(arr):
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    return mex

test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    mex = find_mex(arr)

    if mex == 0:
        # Special case when MEX is 0, we can always split into two segments
        print(2)
        print(1, 1)
        print(2, size)
        continue

    cnt = 0
    start = 0
    segments = []
    num_set = set()  # To track elements less than MEX
    
    # Process the array and try to form subsegments
    for i in range(size):
        if arr[i] < mex:
            num_set.add(arr[i])
        
        # If we've seen all elements from 0 to mex-1
        if len(num_set) == mex:
            segments.append((start + 1, i + 1))  # Form a subsegment (1-based index)
            start = i + 1  # Start a new segment after this index
            num_set.clear()  # Reset the set to track elements for the next subsegment

    # Final adjustment to the last segment to include the remainder of the array
    if num_set:
        segments[-1] = (segments[-1][0], size)  # Adjust the last segment

    if len(segments) < 2:
        print(-1)  # If fewer than 2 subsegments, no valid division
    else:
        print(len(segments))  # Number of subsegments
        for seg in segments:
            print(seg[0], seg[1])  # Output the subsegments
