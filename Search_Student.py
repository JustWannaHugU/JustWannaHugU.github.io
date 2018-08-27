#!/usr/bin/env python3
n = input('pls input how many students you want to tell me:')
n = int(n)
#list_dic =[]
dic = {}
while n > 0:
	key = input("pls input the student's number:")
	value = input("pls input the students's name:")
	dic[key] = value
	n -= 1
	#list_dic.append(dic)
k = input('pls tell me how many you want to search:')
k = int (k)
#for each in n:
#	print(dic[each])
for i in range(k):
	tmp_key = input('请输入要查询的第{:}个学生的学号：'.format(i+1))
	if tmp_key in dic:
		print(dic[tmp_key])
	else:
		print('Not Found!')

	
