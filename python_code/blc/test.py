testlist = list(range(30))
print(testlist)
another_list = [0 for x in testlist]
index = 0
for x in another_list:
	index += 1
	if x == 0:
		print(testlist[index])

print(testlist)
print(another_list)