votes = []
while True:
    vote = input()  # read each vote
    if vote == '***':  # break the loop if input is ***
        break
    votes.append(vote)  # add the vote to the list

# count the votes for each candidate
vote_count = {}
for vote in votes:
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1

# find the candidate with the most votes
winner = None
max_votes = 0
for candidate, count in vote_count.items():
    if count > max_votes:
        winner = candidate
        max_votes = count

# check if the winner has a simple majority
if max_votes / len(votes) > 0.5:
    print(winner)
else:
    print("Runoff!")