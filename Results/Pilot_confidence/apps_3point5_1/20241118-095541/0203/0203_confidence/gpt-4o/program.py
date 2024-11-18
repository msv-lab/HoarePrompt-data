n = int(input())
votes = input().strip()

# Queues to track the positions of 'D' and 'R'
d_queue = []
r_queue = []

# Populate the initial queues with the index of each 'D' and 'R'
for i, v in enumerate(votes):
    if v == 'D':
        d_queue.append(i)
    else:
        r_queue.append(i)

# Process the queues until one of them is empty
while d_queue and r_queue:
    d_index = d_queue.pop(0)
    r_index = r_queue.pop(0)
    
    # The smaller index (earlier in the sequence) eliminates the other
    if d_index < r_index:
        d_queue.append(d_index + n)
    else:
        r_queue.append(r_index + n)

# Determine the winner based on the remaining non-empty queue
if d_queue:
    print('D')
else:
    print('R')
