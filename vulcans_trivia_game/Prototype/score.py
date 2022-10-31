from time import time

class Score:
    def __init__(self):
        self.timer = True
        self.reset()

    def reset(self):
        self.correct = []
        self.incorrect = []
        self.time = None
        self.timeEnd = None

    def startTime(self):
        self.time = time()
    def endTime(self):
        self.timeEnd = time()
    def getTime(self):
        return round(float(self.timeEnd-self.time))

    def toggleTimer(self):
        self.timer = not self.timer

    def getResults(self):
        if self.timer:
            return f'Correct: {self.getNumCorrect()} out of {self.getNumAns()}\n Total Time: {self.getTime()}s'
        else:
            return f'Correct: {self.getNumCorrect()} out of {self.getNumAns()}'

    def getNumCorrect(self):
        return len(self.correct)

    def getNumIncorrect(self):
        return len(self.incorrect)

    def getPercent(self):
        PERCISION = 0
        
        percent = float(self.getNumCorrect())/self.getNumAns()
        percent *= 100
        if PERCISION:
            percent = round(percent,PERCISION)
        else:
            percent = round(percent)
        return percent

    def getCorrect(self):
        return self.correct

    def getIncorrect(self):
        return self.incorrect

    def addCorrect(self, question):
        self.correct.append(question)

    def addIncorrect(self, question):
        self.incorrect.append(question)

    def getNumAns(self):
        return self.getNumCorrect() + self.getNumIncorrect()