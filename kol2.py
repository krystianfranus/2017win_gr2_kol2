# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from lib import Student, Course



if __name__ == "__main__":

	maths = Course(name='Maths', max_no_students=32)
	physics = Course(name='Physics', max_no_students=30)
	computer_science = Course(name='Computer science', max_no_students=31)

	student1 = Student(first_name='Tom', last_name='Perry')
	student2 = Student(first_name='John', last_name='Smith')

	courses = [maths, physics, computer_science]
	students = [student1, student2]

	maths.add_student(student1)
	physics.add_student(student2)
	computer_science.add_student(student1)
	computer_science.add_student(student2)


	print 'Welcome in our school.'


	while(True):

		print 'What do you want to do?\n0) Exit\n1) Print all courses\n2) Print all students' 

		x = int(input('Response: '))

		if(x == 0):
			break

		if(x == 1):
			for course in courses:
				print '-' + str(course)

		if(x == 2):
			for student in students:
				print '-' + str(student)






	

