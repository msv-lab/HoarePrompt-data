n = int(raw_input())
prize_indexes = raw_input()
prize_indexes = [int(x) for x in prize_indexes.split(' ')]

my_seconds = 0
friends_seconds = 0
for i in prize_indexes:
	if i <= 5*10**5:
		my_seconds = i - 1
	else:
		friends_seconds = 10**6 - i

print (max(my_seconds, friends_seconds))


