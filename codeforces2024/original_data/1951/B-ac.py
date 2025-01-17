
def read_tests():
	data = input()
	return int(data)

def read_one_test():
	data = input()
	data_splitted = data.split()

	cows, my_cow_pos = int(data_splitted[0]), int(data_splitted[1])

	ratings_line = input()
	ratings = []	

	for rating in ratings_line.split():
		ratings.append(int(rating))

	return (my_cow_pos - 1, ratings)

def find_higher_ratings(ratings, my_rating_idx):
	ratings_len = len(ratings)
	my_rating = ratings[my_rating_idx]
	first_higher_idx = None
	second_higher_idx = None

	for i in range(ratings_len):
		if (ratings[i] > my_rating):
			if first_higher_idx is None:
				first_higher_idx = i
			else:
				second_higher_idx = i
				break

	return (first_higher_idx, second_higher_idx)

def count_wins(my_idx, first_higher_idx, second_higher_idx, ratings_len):
	if first_higher_idx is None and second_higher_idx is None:
		return ratings_len - 1
	else:
		if first_higher_idx < my_idx:
			# check swap with beggining or with higher rating
			wins_before_first = first_higher_idx - 1
			wins_after_first = None
			if second_higher_idx is not None:
				if second_higher_idx < my_idx:
					# wins between first and second higher ratings
					wins_after_first = second_higher_idx - first_higher_idx
				else:
					# wins between initial first higher rating and my rating
					wins_after_first = my_idx - first_higher_idx
			else:

				wins_after_first = my_idx - first_higher_idx

			if first_higher_idx == 0:
				wins_after_first -= 1

			return max(wins_before_first, wins_after_first)
		else:
			#swap with beggining
			return first_higher_idx - 1


tests_num = read_tests()

for i in range(tests_num):
	my_idx, ratings = read_one_test()
	first_idx, second_idx = find_higher_ratings(ratings, my_idx)
	best_case = count_wins(my_idx, first_idx, second_idx, len(ratings))
	print(best_case)



