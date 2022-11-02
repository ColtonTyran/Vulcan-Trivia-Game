import sys
import tkinter as tk
import pygame
from question import Question
from questions import Questions
from tkinter import *
#from Prototype.questions import Questions
from genre import Genre
from score import Score
from random import choice
from moviepy.editor import *

# This deals with windows/linux file path
native_separator = '\\' if sys.platform == 'win32' else "/"

# Window data
gameTitle = "Vulcan's Trivia Game"
SIZE = '900x500'
BG = ['gray15','gray80']
# stands for Menu Button Color, and it switches with light/dark mode
MBC = ['grey33','steel blue']
# stands for Question Font Color, it makes the questions more viewable between light/dark mode, this is also applied to
# text that stands against to background so that they are easily visible depending on light/dark mode
QFC = ['white','black']
colors = ['blue', 'green', 'red', 'yellow', 'orange', 'purple', 'chocolate1']

# Global data
NUM_QUESTIONS = 10
light_mode = True
selected_genre = None

# Fonts
class Fonts:
	title = 'helvetica 40 bold'
	subtitle = 'helvetica 20 bold'
	text = 'helvetica 30 bold'
	text_large = 'helvetica 40 bold'
	text_small = 'helvetica 15'
	button = 'helvetica 30 bold'
	button_small = 'helvetica 20 bold'

# Set up window
root = tk.Tk()
root.title('Made by Gabriel Simon, Colton Tyran, and Alex Walker')
root.geometry(SIZE)
root.resizable(0,0)

# Question files
FILES = ['StarTrek_Questions.txt', 'StarWars_Questions.txt', 'Marvel_Questions.txt', 'DC_Questions.txt']
FILE_PATHS = ["questions"+native_separator+files for files in FILES]
#FILE_PATHS = [".."+native_separator+"questions"+native_separator+files for files in FILES]
DEBUG = "debug"+native_separator+'debug_questions.txt'
#DEBUG = ".."+native_separator+'debug'+native_separator+'debug_questions.txt'
FILE_PATHS.append(DEBUG) 
FILE_PATHS.append("") # was added for header file
FILE_PATHS.append("") # for Intro 

# Images
PNGS = ["StarTrek_Logo.png", "StarWars_Logo.png", "Marvel_Logo.png", "DC_Logo.png", "Vulcan_Game_Intro.png", "Vulcan_Header.png"]
PNG_PATHS = ["images"+native_separator+png for png in PNGS]
#PNG_PATHS = [".."+native_separator+"images"+native_separator+png for png in PNGS]
IMAGES = [PhotoImage(file=png) for png in PNG_PATHS]
IMAGES.insert(4,'') # For debug

# Genres
GENRES = [Genre(file, img) for file, img in zip(FILE_PATHS, IMAGES)]

# Questions and score
questions = Questions()
results = Score()

# loading screen
def streamVideo():
	clip = VideoFileClip('videos/Vulcan_Intro.mp4')
	#clip = VideoFileClip(".."+native_separator+"Prototype"+native_separator+"videos"+native_separator+"Vulcan_Intro.mp4")
	clip.preview()
	pygame.quit()

# Main Menu Page
def main_menu():
    # Clear screen
    clear()
    clearGenre()
    root.configure(bg = BG[light_mode])
    displayLogo = Label(root, image = GENRES[5].image, bg = 'black')
    startButton = tk.Button(root, text = "Click Here To Play!", fg = 'white', bg = MBC[light_mode], command=main_hub)
    settingsButton = tk.Button(root, text = "Settings", fg = 'white', bg = MBC[light_mode], command=settings)
    
    # Pack widgets
    displayLogo.place(x=0,y=0)
    startButton.place(x=400, y=462)
    settingsButton.place(x=835, y=462)

# Settings Page    
def settings():
    # Clear screen
    clear()
    root.configure(bg = BG[light_mode])
    # clear results
    header = Label(root, image = GENRES[6].image, bg = 'black')
    displayName = tk.Label(root, text="Settings!", font = Fonts.subtitle, fg = QFC[light_mode], bg = BG[light_mode])
    settingButtons = []
    settingButtons.append(tk.Button(root, text = "  Dark Mode   " if light_mode else "   Light Mode  ", fg = 'white', font = Fonts.text, bg = MBC[light_mode], command=toggleLight))
    settingButtons.append(tk.Button(root, text = "Disable Timer" if results.timer else "Enable Timer ", font = Fonts.text, fg = 'white', bg = MBC[light_mode], command=toggleTimer))
    settingButtons.append(tk.Button(root, text = "How to play" , font = Fonts.text, fg = 'white', bg = MBC[light_mode], command = tutorial))
    settingButtons.append(tk.Button(root, text = "Description ", font = Fonts.text, fg = 'white', bg = MBC[light_mode], command=info))
    settingButtons.append(tk.Button(root, text = "    Credits    ", font = Fonts.text, fg = 'white', bg = MBC[light_mode], command=credits))
    homeButton = tk.Button(root, text='Home', fg = 'white', bg = MBC[light_mode], command=main_menu)
    
    # Pack widgets
    header.place(x=0,y=0)
    displayName.place(x=400, y=85)
    but_pos = [(100,150), (100,260), (525,150), (525, 260), (525, 370)]  # x,y pos for genre place
    for but, pos in zip(settingButtons, but_pos):
        but.place(x=pos[0], y=pos[1])
    homeButton.place(x=835, y=460)

# Main Hub for selecting Genre
def main_hub():
	# Clear screen
	clear()
	root.configure(bg = BG[light_mode])
	# clear results
	results.reset()
	clearGenre()
	header = Label(root, image = GENRES[6].image, bg = 'black')
	genreButtons = []
	genreButtons.append(tk.Button(root, image = GENRES[0].image, bg = 'black', command=lambda:selectGenre(0)))
	genreButtons.append(tk.Button(root, image = GENRES[1].image, bg = 'black', command=lambda:selectGenre(1)))
	genreButtons.append(tk.Button(root, image = GENRES[2].image, bg = 'black', command=lambda:selectGenre(2)))
	genreButtons.append(tk.Button(root, image = GENRES[3].image, bg = 'black', command=lambda:selectGenre(3)))
	debugButton = tk.Button(root, text='Debug', fg = 'white', bg = 'black', command=lambda:selectGenre(4))
	multiButton = tk.Button(root, text= 'Multi', fg = 'white', bg = 'purple', command=lambda:selectGenre(5))

	# Pack widgets
	header.place(x=0,y=0)
	but_pos = [(110,105), (460,105), (110,300), (460,300)]  # x,y pos for genre place
	for but, pos in zip(genreButtons, but_pos):
		but.place(x=pos[0], y=pos[1])

	debugButton.place(x=835, y=460)
	multiButton.place(x=790, y=460)

# Number of Questions
def choose_Num_Questions():
	#clear screen
	clear()
	root.configure(bg = BG[light_mode])
	header = Label(root, image = GENRES[6].image, bg = 'black')
	subTitle = tk.Label(root,text="Click on how many questions you would like!", font = Fonts.subtitle, fg = QFC[light_mode], bg = BG[light_mode])
	genreButtons = [] 
	genreButtons.append(tk.Button(root, text = "5 Questions  ", font = Fonts.text, bg = MBC[light_mode], fg = 'white', command=lambda:setQuizSize(5)))
	genreButtons.append(tk.Button(root, text = "10 Questions", font = Fonts.text, bg = MBC[light_mode], fg = 'white', command=lambda:setQuizSize(10)))
	genreButtons.append(tk.Button(root, text = "15 Questions", font = Fonts.text, bg = MBC[light_mode], fg = 'white', command=lambda:setQuizSize(15)))
	genreButtons.append(tk.Button(root, text = "20 Questions", font = Fonts.text, bg = MBC[light_mode], fg = 'white', command=lambda:setQuizSize(20)))
	homeButton = tk.Button(root, text='Home', fg = 'white', bg = MBC[light_mode], command=main_menu)

	#pack widgets
	header.place(x=0,y=0)
	subTitle.place(x=150, y=85)
	but_pos = [(100,150), (100,260), (525,150), (525, 260),]  # x,y pos for genre place
	for but, pos in zip(genreButtons, but_pos):
		but.place(x=pos[0], y=pos[1])
	homeButton.place(x=835, y=460)

# back end of trivia game
def triviaGame(q):
	questionNum = results.getNumAns() + 1
	totalQuestions = questions.quizSize

	# Create widgets
	header = Label(root, image = GENRES[6].image, bg = 'black')
	questionCount = tk.Label(root,text=f"Question: {questionNum}/{totalQuestions}", font = Fonts.subtitle, fg = 'white', bg = 'slate grey')
	questionBox = tk.Label(root, text=q.getQ(), wraplength = 400, font = Fonts.subtitle, fg= QFC[light_mode], bg = BG[light_mode])
	trueBut = tk.Button(root, text="TRUE", font = Fonts.button, fg='white', bg='green3', command=lambda:clickAnswer(q, True))
	falseBut = tk.Button(root, text='FALSE', font = Fonts.button, fg='white', bg='red3', command=lambda:clickAnswer(q, False))
	homeButton = tk.Button(root, text='Home', fg = 'white', bg = MBC[light_mode], command=main_menu)
    
  
	header.pack(ipadx=0,ipady=0, fill = 'x')
	questionCount.pack(ipadx=5, ipady=5, fill = 'x')
	questionBox.pack(ipadx=10, ipady=10, fill = 'x')
	trueBut.place(x=130, y=330)
	falseBut.place(x=600, y=330)
	homeButton.place(x=835, y=460)


def clickAnswer(q, a):
	res = None
	# Bitwise check for correct answer
	# T T -> T
	# T F -> F
	# F T -> F
	# F F -> T
	res = not q.getA() ^ a

	# Update global results
	if res:
		results.addCorrect(q)
	else:
		results.addIncorrect(q)

	# Show result of question
	showRes(res)


def showRes(res):
	global results
	# Clear answers
	clearAns()

	# Create output label
	output = 'Correct!' if res else 'Incorrect'
	outputLabl = tk.Label(root,text=output, borderwidth=10, font = Fonts.text, bg='green3' if res else 'red3', fg='white')
	outputLabl.pack(ipadx=0, ipady=0, expand=True, fill='both')

	#Create next question button

	if not questions.isEmpty():
		NextBut = tk.Button(root, text="NEXT", borderwidth=2, font = Fonts.button_small, bg = MBC[light_mode], command=nextQuestion)
		NextBut.pack(ipadx=10, ipady=10, fill='x')

	# If no more questions show results
	else:
		if results.timer:
			results.endTime()
		ResBut = tk.Button(root, text="RESULTS", borderwidth=2, font = Fonts.button_small, bg = MBC[light_mode], command=printResults)
		ResBut.pack(ipadx=10, ipady=10, fill='x')


def nextQuestion():
	# Clear screen
	clear()
	# Set next
	next_question = questions.getNextQuestion()
	# Start next question
	triviaGame(next_question)

def showPlayQuit():
	# Create and pack a retry button
	playAgain = tk.Button(root, text='Play Again', bg = 'green', fg='white', font=Fonts.button_small, command=main_menu)
	playAgain.place(x=100, y=400)

	# Create and pack quit
	quit = tk.Button(root, text='      Quit      ', bg = 'red4', fg='white', font=Fonts.button_small, command=root.quit)
	quit.place(x=625, y=400)

# Results Page
def printResults():
	clear()
	# Get total correct
	root.configure(bg = BG[light_mode])

	# Get percent right
	percent = results.getPercent()
 
	header = Label(root, image = GENRES[6].image, bg = 'black')
	header.pack(ipadx=0, ipady=0, fill = 'x')

	# Check if score is above a certain threshold, and create a separate message for each case
	if (percent == 100):
		endLabl = tk.Label(root, text='Wow, perfect game!', fg = QFC[light_mode], bg = BG[light_mode], font=Fonts.text)
	elif(percent >= 90 ) and (percent <= 99):
		endLabl = tk.Label(root, text='Excellent knowledge, great game!', fg = QFC[light_mode], bg = BG[light_mode], font=Fonts.text)
	elif(percent >= 80) and (percent <= 89):
		endLabl = tk.Label(root, text='Good game!', fg = QFC[light_mode], bg = BG[light_mode], font=Fonts.text)
	elif(percent >= 70) and (percent <= 79):
		endLabl = tk.Label(root, text='You passed!', fg = QFC[light_mode], bg = BG[light_mode], font=Fonts.text)
	else:
		endLabl = tk.Label(root, text='Better luck next time.', fg = QFC[light_mode],  bg = BG[light_mode], font=Fonts.text)

	# Create result widgets
	scoreLabl = tk.Label(root, text=f'{results.getResults()}', fg='red', bg = BG[light_mode], font=Fonts.button_small)
	percentLabl = tk.Label(root, text= f'{percent}%', fg = QFC[light_mode], bg = BG[light_mode], font=Fonts.text_large)

	# Pack result widgets
	endLabl.pack(ipadx=10, ipady=10)
	scoreLabl.pack(ipadx=10, ipady=10)
	percentLabl.pack(ipadx=10, ipady=10)

	# Create see answers button
	answers = tk.Button(root, text='Answers', fg='black', bg = MBC[light_mode], font=Fonts.button_small, command=showAnswers)
	answers.place(x=375, y=335)

	retestBut = tk.Button(root, text='  Retest  ', fg='black', bg = MBC[light_mode], font=Fonts.button_small, command=retest)
	retestBut.place(x=375, y=400)
	showPlayQuit()

def retest():
	results.reset()
	questions.retestQuestions()
	start()


def clearAns():
	# Clear all but question label
	widgets = root.pack_slaves()
	for i in range(1, len(widgets)):
		widgets[i].destroy()


def clear():
	# Clear all widgets
	for widget in root.pack_slaves():
		widget.destroy()
	for widget in root.place_slaves():
		widget.destroy()


# Read questions from file -> List(questions)
def getQuestions(file):
	new_questions = []
	with open(file, 'r') as f:
		new_questions = f.readlines()
	return new_questions

# Set questions and size
def setQuestions(new_questions):
	questions.setSize(NUM_QUESTIONS)		# set size of quiz
	questions.setQuestions(new_questions)	# set questions

# Allow choices from all genres
def multiGenre():
	questions = []
	for genre in GENRES:
		if genre.file != DEBUG and genre.file != None:		# All but debug
			for q in getQuestions(genre.file):
				questions.append(q)
	setQuestions(questions)


# Set number of questions to be tested
def setQuizSize(num):
	global NUM_QUESTIONS
	NUM_QUESTIONS = num

	start()


# Seklect genre for questions
def selectGenre(num):
	clear()
	clearGenre()
	global selected_genre

	if num > 4:
		clearGenre()
		choose_Num_Questions()
	elif num == 4:
		selected_genre = GENRES[num]
		setQuizSize(3)
	else:
		selected_genre = GENRES[num]        # set genre to index of genre
		choose_Num_Questions()

# Start game
def start():
	if results.timer:
		results.startTime()		# start time

	if selected_genre:
		questions = getQuestions(selected_genre.file)   # get questions from genre file
		setQuestions(questions)
	else:
		multiGenre()					# if no genre selected do multi
	nextQuestion()        				# display first question

def clearGenre():
	global selected_genre 
	selected_genre= None

def showAnswers():
	clear()


	# Get correct and incorrect
	incorrect = results.getIncorrect()
	correct = results.getCorrect()

	# Create incorrect label
	incLabl = tk.Label(root, text='  INCORRECT:  ', fg='white', bg='red', font=Fonts.subtitle)
	inc_labels = [tk.Label(root, wraplength = 850, text=f'{str(q)}', fg=QFC[light_mode], bg = BG[light_mode], font=Fonts.text_small) for q in incorrect]
	incLabl.pack(ipadx=0, ipady=0)
	for label in inc_labels:
		label.pack(ipadx=10, ipady=0, fill='x')

	# Create correct label
	corLabl = tk.Label(root, text='   CORRECT:   ', fg='white', bg='green', font=Fonts.subtitle)
	cor_labels = [tk.Label(root, wraplength = 700, text=f'{q.getQ()}', fg=QFC[light_mode], bg = BG[light_mode], font=Fonts.text_small) for q in correct]
	corLabl.pack(ipadx=0, ipady=0,)
	for label in cor_labels:
		label.pack(ipadx=10, ipady=0, fill='x')

	retestBut = tk.Button(root, text='  Retest  ', fg='black', bg = MBC[light_mode], font=Fonts.button_small, command=retest)
	retestBut.pack(ipadx=10, ipady=10)

	showPlayQuit()

# Toggle between light and dark
def toggleLight():
	global light_mode
	light_mode = not light_mode
	settings()

# Toggle between timer on and off
def toggleTimer():
	results.toggleTimer()
	settings()

# Show game info
def info():
	clear()
	menu = tk.Label(root,text=gameTitle, font = Fonts.title, fg = 'white', bg = 'black')
	root.configure(bg = BG[light_mode])
	info_text = 'Hello! This is a multi-genre trivia Game.\nChoose a genre, test your knowledge, and have fun!\nTry to see if you can get a perfect score.'

	menu.pack(ipadx=0, ipady=0, fill = 'x')
	info_labl = tk.Label(root, wraplength = 800, text=info_text, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text)
	info_labl.pack(ipadx=10, ipady=0, fill='x', expand=True)
	homeButton = tk.Button(root, text='Home', fg = 'white', bg = MBC[light_mode], command=main_menu)
	homeButton.place(x=835, y=460)
 
# How to Play in Settings 
def tutorial():
	clear()
	root.configure(bg = BG[light_mode])
	step_1 = "Step 1: Select any genre"
	step_2 = "Step 2: Select number of questions"
	step_3 = "Step 3: Read question"
	step_4 = "Step 4: Choose 'true' or 'false'"
	step_5 = "Step 5: Click 'next' to go to next question"
	step_6 = "Step 6: See results/Play again"
 
	steps = []
	steps.append(tk.Label(root, text = step_1, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text)) 
	steps.append(tk.Label(root, text = step_2, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text))
	steps.append(tk.Label(root, text = step_3, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text))
	steps.append(tk.Label(root, text = step_4, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text))
	steps.append(tk.Label(root, text = step_5, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text))
	steps.append(tk.Label(root, text = step_6, fg=QFC[light_mode], bg=BG[light_mode], font=Fonts.text))
	menu = tk.Label(root,text=gameTitle, font = Fonts.title, fg = 'white', bg = 'black')
	homeButton = tk.Button(root, text= "Home", fg = 'white', bg = MBC[light_mode], command=main_menu)
 
	menu.pack(ipadx=0, ipady=0, fill = 'x')
	but_pos = [(30,72.5), (30,145), (30,217.5), (30, 290), (30, 362.5), (30, 435)]  # x,y pos for genre place
	for step, pos in zip(steps, but_pos):
		step.place(x=pos[0], y=pos[1])
	homeButton.place(x=835, y=460)
    

# Show developer credits
def credits():
	clear()
	root.configure(bg =BG[light_mode])

	developers = []
	alex = 'Alex Walker a_w366@txstate.edu'
	developers.append(alex)
	gabriel = 'Gabriel Simon gms139@txstate.edu'
	developers.append(gabriel)
	colton = 'Colton Tyran ctt32@txstate.edu'
	developers.append(colton)
 
	menu = tk.Label(root,text=gameTitle, font = Fonts.title, fg = 'white', bg = 'black')
	menu.pack(ipadx=0, ipady=0, fill = 'x')

	dev_labels = []
	for dev in developers:
		dev_labels.append(tk.Label(root, text=dev, fg=choice(colors), bg= BG[light_mode], font=Fonts.text))
	for d_labl in dev_labels:
		d_labl.pack(ipadx=10, ipady=10, fill='x')

	homeButton = tk.Button(root, text='Home', fg = 'white', bg = MBC[light_mode], command=main_menu)
	homeButton.place(x=835, y=460)


# Play game
def main():
    # v0.1 was sprint 1, v0.2 was sprint 2
	print('Launching Vulcan Trivia Game v0.2')
	# show game intro
	streamVideo()
	# ensures there is nothing in the screen
	clear()
	# Main menu
	main_menu()
	# GUI loop
	root.mainloop()
	# Terminate
	print('Thank you for playing!')
	
if __name__ == '__main__':
	main()