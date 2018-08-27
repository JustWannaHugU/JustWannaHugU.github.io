#!/usr/bin/env python3
def cal_num(id):
	list_id = list(id)
	list_value = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
	sum_17 = 0
	for i in range(17):
		tmp = int(list_id[i]) * list_value[i]
		sum_17 += tmp
	mod_num = sum_17 % 11#余数已经求出
	list_cur = [1,0,'X',9,8,7,6,5,4,3,2]
	cal_num = list_cur[mod_num]
	return cal_num

id = input('pls input your personal_card nuberd:')
if int(id[17]) == cal_num(id):
	print('Right personnal Card number!!')
else:
	print('Wrong number!!')


