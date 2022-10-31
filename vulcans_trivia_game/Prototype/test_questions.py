from questions import Questions
import unittest

class QuestionsTest(unittest.TestCase):
    test_questions = ['hello has 5 letters-1', 'violets are blue-1', 'Penguins can fly-0']

    print("Running test for empty Question class")

    def testIsEmpty(self):
        q = Questions()

        if self.assertTrue(q.isEmpty()):
            print("Question class is empty")

        q.addQuestion(self.test_questions[0])
        if self.assertFalse(q.isEmpty()):
            print("Question class has some information.")

    print("Running test for list of questions to pick from.")

    def testAddQuestion(self):
        q = Questions()

        q.addQuestion(self.test_questions[1])

        if self.assertEqual(q.numQuestions, 1):
            print("Added question to Question class.")
        self.assertFalse(q.isEmpty())

    print("Running test to select question.")

    def testSetQuestions(self):
        q = Questions()

        q.setQuestions(self.test_questions)

        self.assertEqual(q.numQuestions, 3)
        self.assertFalse(q.isEmpty())
        if self.assertEqual(q.getNextQuestion().q, 'hello has 5 letters'):
            print("Question was correctly selected.")

    print("Running test to select next question.")

    def testGetNextQuestion(self):
        q = Questions()

        q.setQuestions(self.test_questions)

        self.assertEqual(q.numQuestions, len(self.test_questions))
        if self.assertEqual(q.getNextQuestion().q, 'hello has 5 letters'):
            print("Next question was correctly selected.")
        self.assertFalse(q.isEmpty())

    print("Running test to confirm that Question class won't hold duplicates,")

    def testCheckTwoQuestions(self):
        q1 = Questions()
        q2 = Questions()

        q1.addQuestion(self.test_questions[1])
        q2.addQuestion(self.test_questions[2])

        if self.assertNotEqual(q1, q2, 'Questions are the same.'):
            print("Questions are different.")


def main():
    unittest.main()
    main()
