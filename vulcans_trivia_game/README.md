# Project Name - Vulcan's Trivia Game
- Created by Colton Tyran, Alex Walker, and Gabriel Simon
- A trivia game on well known genres in pop culture.
- Was created for trivia enthusists. 
- Doing this for a fun game and practice among software engineering practice with a team and using agile methods.
​
## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Sprint1](#sprint1)
* [Sprint2](#sprint2)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
​
## General Information
- An application trivia game with multiple category selections.
- The user may select one of four 5/10/15/20 question categories.
- After a series of true or false questions, the user will get their results and correct answers.
- It is intended for enthusiests to test their knowledge through an exciting and fun quiz.
​
## Technologies Used
- Jira/Bitbucket/Discord/Slack for planning and team communication.
- GitKraken for source control and team remote repository.
- Tkinter python package for GUI
- PyUnit to run tests on our progress builds.
- Pygame and MoviePy for loading screen integration
​
## Features
- Multiple genre category
- Immediate user feedback
- Competitive score keeper
- Results and correct answers revealed following the quiz
- Replayable with different category
- 5/10/15/20 Question modes
- Multi-Genre mode
- Randomized pool of questions
- Game timer
- Light/Dark mode
- How to Play in settings
- Description of Game in settings
- Credits Page with randomized color text
- Small selection of settings to customize user experience
- Debug option for user tests while creating game

## Screenshots
* [Main Menu](https://i.gyazo.com/65e2e40a3c2c86a00356f570be0dc6ec.png)
* [Main Hub](https://i.gyazo.com/6f5eac5dd3a5d137e0e87f934da55d6c.png)
* [Settings Page](https://i.gyazo.com/4b112c5601a2308bb60f5d6ca150196b.png)
* [Dark mode/Settings Page](https://i.gyazo.com/7a22c1da52e4209023e9d38bd88984ee.png)
* [Number of Question Selection Page](https://i.gyazo.com/d082185df30e4f44399590b4f43a0c9e.png)
* [Question Example](https://i.gyazo.com/96d7a4f0f9760637664e1248e6233527.png)
* [Correct Answer](https://i.gyazo.com/5ed7ce4ed95b6c06639b49a60fdb12d3.png)
* [Incorrect Answer](https://i.gyazo.com/1c0756e935604f0216181e03484dcd84.png)
* [Results Page](https://i.gyazo.com/07dacc62f167cabe1427dba910c22f34.png)
* [Answers Page](https://i.gyazo.com/df86e49883fc45056dfa6d8d35dd8e00.png)

## Sprint1
- Colton Tyran 
	- Created GUI for game (Main Menu,Question/Answer,Results), edited end screen, and created all questions for each genre
- Alex Walker 
	- Created Questions Class, score and percentage logic, logical functions between Gui and classes, question counter, and show correct/incorrect answers
- Gabriel Simon 
	- Created GUI for end screen, decided on what genres to use, establish CircleCI and setup pytests

## Sprint2
Each team member completed the following tasks and each branch associated with the changes have been included.

- Colton Tyran
	- Created and implemented a loading screen (VTG-36-loading-screen), created and implemented a main menu (VTG-29-main-menu), created a selection page for 5/10/15/20 question mode (VTG-30-add-5-10-15-20-question-page), added a settings page/home button for navigation (VTG-31-home-button), polished GUI, and added a game header (VTG-8-gui-polish).
- Alex Walker 
	- Created Home button and implementation (feature/VTG-42-create-button-implementation-for-), created and implemented retest/replay buttons (feature/VTG-34-retest-replay-buttons), created and implemented mixed-genre mode (feature/VTG-37-mixed-genre-mode7), implemented 5/10/15/20 question modes (feature/VTG-38-create-5-10/15/20-question-game-m), implemented game time (VTG-33-game-timer), implemented duplicate question protection (feature/VTG-32-duplicate-question-protection).
- Gabriel Simon 
	- Fixed CircleCI and Interoperability issues (VTG-41-update-circleci-for-new-layout, Interoperabilty fixes linked to one branch with Dr. Lehr's approval), expanded question pools to 50 in each genre (feature/VTG-27-expand-questions-pool), set up light/dark mode color schemes to ensure readability (VTG-28-light-dark-mode-polish).
​
## Setup
- 1) Clone the BokoBot repository : git clone https://a_w366@bitbucket.org/cs3398-s22-vulcans/vulcans_trivia_game.git
- 2) Install pygame and moviepy in terminal ("pip install pygame" "pip install moviepy")
- 3) Run the command "python3 Prototype/trivia.py" from the main directory
- 4) Click close or quit button to exit

## Usage
- 1) Select any genre
- 2) Select number of questions
- 3) Answer question with button click of "True" or "False"
- 4) Click next to get next question
- 5) Continue testing your knowledge until no more questions remain.
- 6) See your results
- 7) Click close or quit button to exit

## Project Status
- Project is: *in progress*
* [Want to play? Click Here!](https://replit.com/@AlexWalker5/VulcanTriviaGame)   This is currently not available! 
- Prototype is stable for running and testing, please look at [setup](#setup) to play

## Room for Improvement
- Dynamically added question through internet website searches
- Question pool expanded
- Multiple choice questions
- Background music/sound effects
- Difficulty options
- More genres
- More settings options
- Record of previous playthroughs

## Acknowledgements
- This project was inspired by Colton Tyran, Alex Walker, and Gabriel Simon gaming needs.
- Many thanks to Dr. Lehr for the opportunity to create this project.
​
## Contact
- Created by Colton Tyran(ctt32@txstate.edu), Alex Walker(a_w366@txstate.edu), Gabriel Simon(gms139@txstate.edu)
