def print_list(num,students):
	a = 0
	print("number of student:",num, "/",len(students))
	for y in students:
		a += 1
		print(y,end=" ")
		if a % 5 == 0:
			print()
	a = 0
	print()


notnumber = False
number_of_students = 0
while not notnumber:
	try:
		number_of_students = int(input("How many student are in this classroom? > "))
		notnumber = True
		print()
	except:
		print("Wrong input!!!!!")



students = list()
for x in range(number_of_students):
	students.append(0)
print_list(0, students)

student_in = -1 
while (input("Check in? y/n > ") != "n"):
	if(student_in+1) < len(students):
		student_in += 1
		students[student_in] = 1
		print_list(student_in+1,students) 
	else:
		print("All students presented!")
		break
student_in += 1
print(student_in, "students presented ", end=" ")
if student_in < len(students):
	print((len(students) - student_in), "did not present")
	index = 1
	did_not_present = list()
	for x in students:
		if x == 0:
			did_not_present.append(index)
		index+= 1
	print(did_not_present, "did not present")
print("Attandance rate",((student_in/len(students)) * 100), "%")