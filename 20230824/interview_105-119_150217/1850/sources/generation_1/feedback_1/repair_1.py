def calculate_best_ranking(D, current_ranking, point_awards):
    # Calculate the points of the astronaut before the race
    points_before_race = current_ranking[D-1]
    
    # Calculate the points awarded in the race
    points_awarded = point_awards[D-1]
    
    # Check if the astronaut can overtake any other ranking positions
    best_ranking = D
    for i in range(D, len(current_ranking)):
        if current_ranking[i] >= points_before_race + points_awarded:
            break
        else:
            best_ranking += 1
    
    return best_ranking


# Read the input
N, D = map(int, input().split())
current_ranking = list(map(int, input().split()))
point_awards = list(map(int, input().split()))

# Calculate the best possible ranking for the astronaut after the race
best_ranking = calculate_best_ranking(D, current_ranking, point_awards)

# Print the result
print(best_ranking)