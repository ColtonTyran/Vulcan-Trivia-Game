import unittest

from Prototype.question import Question


class QuestionTest(unittest.TestCase):
	question1 = 'The number 2 is odd-0'
	question2 = 'Roses are red'
	answer2 = 1

	print("Running test 1")
	def testConstructor(self):
		question = Question.from_str(self.question1)

		self.assertEqual(question.q, 'The number 2 is odd')
		self.assertFalse(question.a)

	print("Running test 2")
	def testSetter(self):
		question = Question.from_str(self.question1)
		question.setQ(self.question2)
		question.setA(self.answer2)

		self.assertEqual(question.q, 'Roses are red')
		self.assertTrue(question.a)

	print("Running test 3")
	def testGetter(self):
		question = Question.from_str(self.question1)
		
		self.assertEqual(question.getQ(), 'The number 2 is odd')
		self.assertFalse(question.getA())

def main():
	
	unittest.main()

main()