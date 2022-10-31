from score import Score
import unittest

class ScoreTest(unittest.TestCase):
	def setUp(self):
		self.score = Score()


	def testReset(self):
		self.score.reset()

		self.assertEqual(len(self.score.correct), 0)
		self.assertEqual(len(self.score.incorrect), 0)

	def testGetNumCorrect(self):
		self.score.reset()
		self.assertEqual(self.score.getNumCorrect(), 0)

		self.score.correct.append(0)
		self.assertEqual(self.score.getNumCorrect(), 1)

	def testGetNumIncorrect(self):
		self.score.reset()
		self.assertEqual(self.score.getNumIncorrect(), 0)

		self.score.incorrect.append(0)
		self.assertEqual(self.score.getNumIncorrect(), 1)

	def testGetPercent(self):
		self.score.reset()

		self.score.correct.append(0)
		self.assertEqual(self.score.getPercent(), 100)

		self.score.incorrect.append(0)
		self.assertEqual(self.score.getPercent(), 50)

	def testGetCorrect(self):
		self.score.reset()

		self.assertEqual(self.score.getCorrect(), [])

		self.score.correct.append(1)
		self.score.correct.append(2)
		self.assertEqual(self.score.getCorrect(), [1,2])

	def testGetIncorrect(self):
		self.score.reset()

		self.assertEqual(self.score.getIncorrect(), [])

		self.score.incorrect.append(1)
		self.score.incorrect.append(2)
		self.assertEqual(self.score.getIncorrect(), [1,2])

	def testAddCorrect(self):
		self.score.reset()

		self.score.addCorrect(0)
		self.assertEqual(self.score.getNumCorrect(), 1)

		self.score.addCorrect(0)
		self.score.addCorrect(0)
		self.assertEqual(self.score.getNumAns(), 3)       

	def testAddIncorrect(self, question):
		self.score.reset()

		self.score.addIncorrect(0)
		self.assertEqual(self.score.getNumIncorrect(), 1)

		self.score.addIncorrect(0)
		self.score.addIncorrect(0)
		self.assertEqual(self.score.getNumAns(), 3)

	def testGetNumAns(self):
		self.score.reset()

		self.assertEqual(self.score.getNumAns(), 0)

		self.score.addCorrect(0)
		self.score.addIncorrect(0)
		self.assertEqual(self.score.getNumAns(), 2)

def main():
	
	unittest.main()

main()