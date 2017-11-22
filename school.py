import numpy as np


class Student:

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Course:
	
	def __init__(self, name, max_no_students=20):
		self.name = name
		self.no_students = 0
		self.max_no_students = max_no_students
		self.students = []
		self.scores = {}

	def add_student(self, student):
		if self.no_students == self.max_no_students:
			print 'Cannot add new student. Limit has been reached.'
		else:
			self.students.append(student)
			self.no_students += 1

	def add_score(self, score, student):
			self.scores[student] = score

	def students_list(self):
		return self.students

	def print_scores(self):
		print 'Students scores in %s:' % (self.name)
		for student, score in self.scores.items():
			print '- %s: %.1f' % (student, score)

	def score_average(self):

		if self.scores:
			average = np.mean([value for key,value in self.scores.items()])
			return average
		else:
			return None
		
	def __str__(self):
		return self.name


