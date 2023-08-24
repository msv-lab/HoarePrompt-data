def minimum_bribes(n, votes):
    limak_index = votes.index(max(votes))  # Find the index of Limak
    limak_votes = votes[limak_index]
    other_votes = votes[:limak_index] + votes[limak_index+1:]
    max_votes = max(other_votes)
    
    if limak_votes > max_votes or votes.count(max_votes) > 1:
        return 0
    
    bribes = max_votes - limak_votes + 1 if max_votes - limak_votes > 0 else 0
    
    return bribes

n = int(input())
votes = list(map(int, input().split()))

bribes_required = minimum_bribes(n, votes)
print(bribes_required)