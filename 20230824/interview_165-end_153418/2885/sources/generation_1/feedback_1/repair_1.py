import json

def insert(intervals, newInterval):
    result = []
    n = len(intervals)
    
    # Add intervals before newInterval
    i = 0
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge intervals with newInterval
    start = newInterval[0]
    end = newInterval[1]
    while i < n and intervals[i][0] <= newInterval[1]:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    
    result.append([start, end])  # add merged newInterval
    
    # Add remaining intervals after newInterval
    while i < n and intervals[i][0] > end:
        result.append(intervals[i])
        i += 1
    
    return sorted(result, key=lambda x: x[0])

intervals = json.loads(input())
newInterval = json.loads(input())

result = insert(intervals, newInterval)
print(result)