def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0]) # update start time of newInterval
        newInterval[1] = max(newInterval[1], intervals[i][1]) # update end time of newInterval
        i += 1
    
    result.append(newInterval) # add merged newInterval
    
    # Add remaining intervals after newInterval
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

intervals = eval(input())
newInterval = eval(input())

result = insert(intervals, newInterval)
print(result)