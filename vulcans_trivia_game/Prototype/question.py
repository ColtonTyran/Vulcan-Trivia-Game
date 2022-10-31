# Question class
class Question:

	# constructor takes question and answer
	def __init__(self, question, answer):
		self.setQ(question)
		self.setA(answer)

	# set question takes question
	def setQ(self, question):
		if type(question) != str:
			question = str(question)
		self.q = question

	# get question prompt
	def getQ(self):
		if self.q == str():
			return 'No question!!'
		return self.q
    
    # set answer takes answer type int, str, or bool
	def setA(self, answer):
		if type(answer) == str:
			self.a = bool(int(answer))
		elif type(answer) == int:
			self.a = bool(answer)
		else:
			self.a = 99
	
	# get answer of question
	def getA(self):
		if self.a == 99:
			return 'No answer!!'
		return self.a

	# contructor given dash seperated str
	@classmethod
	def from_str(cls, question):
		question, answer = question.split('-')
		return cls(question, answer)
	
	# repr
	def __str__(self):
		return(f'{self.getQ()} | {self.getA()}')
