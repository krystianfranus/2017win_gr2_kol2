from school import Student, Course


def initialize_school():
	maths = Course(name='Maths', max_no_students=32)
	physics = Course(name='Physics', max_no_students=30)
	computer_science = Course(name='Computer science', max_no_students=31)

	student1 = Student(first_name='Tom', last_name='Perry')
	student2 = Student(first_name='John', last_name='Smith')
	student3 = Student(first_name='David', last_name='Tao')

	maths.add_student(student1)
	maths.add_student(student2)
	maths.add_score(5.0, student1)
	maths.add_score(4.0, student2)
	#maths.print_scores()
	#print str(maths.score_average())
	#print str(maths.no_students)

	physics.add_student(student1)
	physics.add_student(student2)
	physics.add_score(4.0, student1)
	physics.add_score(3.0, student2)
	#physics.print_scores()
	#print str(physics.score_average())
	#print str(physics.no_students)
	
	computer_science.add_student(student1)
	computer_science.add_student(student2)
	computer_science.add_score(3.0, student1)
	#computer_science.add_score(2.0, student2)
	#computer_science.print_scores()
	#print str(computer_science.score_average())
	#print str(computer_science.no_students)
	
	courses = {'Maths': maths, 'Physics':physics, 'Computer science': computer_science}
	students = {'Tom'+' '+'Perry': student1, 'John'+' '+'Smith': student2, 'David'+' '+'Tao': student3}

	physics.add_student(student2)
	computer_science.add_student(student1)
	computer_science.add_student(student2)

	data = {}
	data['courses'] = courses
	data['students'] = students

	return data
