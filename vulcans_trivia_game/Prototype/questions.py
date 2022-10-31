from random import choice
from question import Question

class Questions():

	def __init__(self):
		self.quizSize = 1
		self.clear()

	# Clear questions and reset count
	def clear(self):
		self.questions = []
		self.removed = []
		self.numQuestions = 0

	# Set size of the quiz
	def setSize(self, size):
		if size > 0 and size < 21:
			self.quizSize = size
		else:
			self.quizSize = 1

	# set questions takes list of dash seperated questions
	def setQuestions(self, questions):
		self.clear()
		while self.numQuestions < self.quizSize:
			q = choice(questions)
			question = Question.from_str(q)
			if not self.checkDuplicate(question):
				self.addQuestion(question)

	# Check if question already in questions
	def checkDuplicate(self, question):
		for q in self.questions:
			if question.getQ() == q.getQ():
				return True
		return False

	# Reset questions back to removed
	def retestQuestions(self):
		questions = self.removed
		self.clear()
		for question in questions:
			self.addQuestion(question)

	# add question to questions
	def addQuestion(self, question):
		self.numQuestions += 1
		self.questions.append(question)

 
 	# check for empty list
	def isEmpty(self):
		return self.numQuestions == 0


	# returns front of queue
	def getNextQuestion(self):
		if self.isEmpty():
			return None
		question = self.questions.pop(0)
		self.removed.append(question)
		self.numQuestions -= 1
		return question
