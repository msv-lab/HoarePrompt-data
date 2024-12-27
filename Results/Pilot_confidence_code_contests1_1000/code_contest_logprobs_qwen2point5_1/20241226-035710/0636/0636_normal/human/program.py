if(__name__ == '__main__'):
	serversCnt = int(raw_input())
	tasks = [int(tmp) for tmp in raw_input().split(' ')]
	total = sum(tasks)
	balancedTask = total // serversCnt
	more = total % serversCnt
	less = total - more
	taskNeedToBalance = 0
	for t in tasks:
		if(t <= balancedTask):
			taskNeedToBalance += balancedTask - t
			if(less > 0):
				less -= 1
			else:
				more -= 1
				taskNeedToBalance += 1
		else:
			taskNeedToBalance += t - balancedTask - 1
			if(more > 0):
				more -= 1
			else:
				less -= 1
				taskNeedToBalance += 1
	print(taskNeedToBalance//2)