import random

def is_head():
	result = random.randint(1,2)
	if(result==1):#head
		return True
	return False


def head_probability():
	head_cnt = 0
	total_experiment_cnt = 50
	for exp in range(total_experiment_cnt): 
		if(is_head()):
			head_cnt += 1

	prob = head_cnt/total_experiment_cnt
	return prob

print(head_probability())