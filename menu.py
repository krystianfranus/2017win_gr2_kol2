import numpy as np

from school import Student, Course

class SchoolMenu():

	def __init__(self, data):
		self.data = data

	def panel(self):
		print '\nWhat do you want to do?\n0) Exit\n1) Show all courses\n2) Add course\n3) Show all students\n4) Add student\n5) Add score\n6) Scores average'

		self.x = raw_input('\nResponse: ')
		print ''

	def response(self):
		return {
			'0': self.exit_system,
			'1': self.menu_courses,
			'2': self.add_course,
			'3': self.menu_students,
			'4': self.add_student,
			'5': self.add_score,
			'6': self.average_score
		}[self.x]

	def exit_system(self):
		print 'Goodbye'
		exit()

	def menu_courses(self):
		for key, value in self.data['courses'].items():
			print '- ' + str(value)

	def add_course(self):
		print 'Add new course'

		name = raw_input('Name: ')
		max_no_students = raw_input('Max number of students: ')
		new_course = Course(name=name, max_no_students=max_no_students)
		self.data['courses'][name] = new_course

	def menu_students(self):
		for key, value in self.data['students'].items():
			print '- ' + str(value)

	def add_student(self):
		print 'Add new student'

		first_name = raw_input('First name: ')
		last_name = raw_input('Last name: ')
		new_student = Student(first_name=first_name, last_name=last_name)
		self.data['students'][first_name] = new_student

	def add_score(self):
		try:
			self.menu_courses()
			pick_course = raw_input('Which course? ')
			course = self.data['courses'][pick_course]

			self.menu_students()
			pick_student = raw_input('Which student? ')
			pick_score = float(raw_input('Score: '))
			course.add_score(pick_score, pick_student)
			course.print_scores()
		except(KeyError):
			print 'ERROR - Wrong course name'

	def average_score(self):
		print '~~ Scores Average in our school ~~'
		print np.mean([course.score_average() for key,course in self.data['courses'].items() if course.score_average()])
		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


