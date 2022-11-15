<kbd>![Minesweeper](/media/logo.PNG)</kbd>

Developer: [Khubab Shamsuddin](https://www.linkedin.com/in/kshamse/)

Live Website: [Minesweeper](https://cli-minesweeper.herokuapp.com/)

![Main Screen](/media/main-screen.PNG)


# Table of Contents

- [Table of contents](#table-of-contents)
- [About Minesweeper](#about-minesweeper)
- [Goals](#goals)
  - [User's Goals](#users-goals)
  - [Site Owner's Goals](#site-owners-goals)
- [User Stories](#user-stories)
    - [User's Stories](#users-stories)
    - [Site Owner's Stories](#site-owners-stories)
- [Game Design](#game-design)
  - [Pseudocode](#pseudocode)
  - [Flowcharts](#flowcharts)
- [Used Technologies](#used-technologies)
  - [Python](#python)
    - [Modules & Packages](#modules-and-packages)
  - [Other Softwares & Tools](#other-softwares-and-tools)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Menus](#menus)
    - [Signup](#signup)
    - [Login](#login)
    - [Game Rules](#game-rules)
    - [About Game](#about-game)
    - [Levels](#levels)
    - [Board](#board)
    - [Symbols and Colors](#symbols-and-colours)
    - [Feedback Messages](#feedback-messages)
  - [Features Left to Implement](#features-left-to-implement)
- [Validation](#validation)
- [Testing](#testing)
  - [Manual](#manual-testing)
  - [Automated](#automated-testing)
- [Bugs](#interesting-bugs)
- [Deployment](#deployment)
- [Credits](#credits)


# About Minesweeper

Minesweeper is a game designed to entertain Internet users. The game board is made up of many columns and rows, and the player must guess and calculate in order to reveal all cells that do not contain mines. The current game is command-line-based, which receives player-guessed cell coordination as input and checks if it has a mine or not. When all cells are revealed, the player wins; if a cell contains a mine, the player loses.

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>

# Goals

## User's Goals

- Play an interesting logic game.

## Site Owner's Goals

- Build an interactive command-line version of the well-known minesweeper game.
- The game should provide amusement and joy to attract more users.

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>

# User Stories

## User's Stories

1. I want to understand the game's rules.
2. I want to be able to control the game's difficulty.
3. I want to get clear feedback on my inputs.
4. I want to be able to review my choices.

## Site Owner's Stories

5. I want the game to be simple and clear.
6. I want the game to have a smooth and natural flow.
7. I want new users to be able to create a new account.
8. I want active users to be able to login to an existing account.
9. I want players to see information about the game and its rules.

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>

# Game Design

## Pseudocode

<details>
  <summary>The Process Steps</summary>

```
1. Display the greeting message.

2. Inquiring about the user's account and providing the options "log in" and "sign up."
    - (2.1) If the user enters "1" for login, he will be asked to enter his credentials.
    - (2.2) If the user enters "2" signup, he will be asked to enter data, and a record will be created as a result.
    - (2.3) The authentication process runs after both of the above options to make sure the user has an account; if authentication fails, inform the user of the wrong email or password and go to "Step 2.1. Login."

3. Display the main menu and await the user's choice (1. start, 2. rules, 3. about).

4. If the user types "1," proceed to "Step 7: Level Selection" to begin the game.

5. Display the game rules and return to "Step 3: Main Menu" if the user enters "2."

6. Display game information and return to "Step 3: Main Menu" if the user enters "3."

7. Display the levels menu and wait for the user to select (1. easy, 2. medium, or 3. difficult).

8. If the user enters "1," proceed to "Step 11: Start the Game" in simple mode.

9. If the user enters "2," proceed to "Step 11: Start the Game" mode.

10. If the user enters "3," proceed to "Step 11: Start the Game" in Hard Mode.

11. Start the game by constructing the board with a specified number of rows and columns, as well as the number of randomly distributed mines based on the level selected.

12. Begin a round by displaying the board.

13. Ask the player to enter the coordination (row and column) of his chosen cell.

14. Display the players' choice.

15. If the chosen cell has been revealed before, inform the user and proceed to "Step 13: Ask for a Guess."

16. Check if the cell contains mine if it's going to "Step 20: End Game."

17. Display the board with the chosen cell containing the number of its neighbouring mines.

18. Check to see if all cells have been explored before proceeding to "Step 20: End Game."

19. Proceed to "Step 12: New Round."

20. If a mine is discovered, show the losing message and the real board; otherwise, show the winning message.

21. Show the "play again" menu (1. yes, 2. no).

22. Proceed to "Step 11: Start the Game" if the user enters "1."

23. Proceed to "Step 3: Main Menu" if the user enters "2."

* Any incorrect selection will result in a feedback message and a new request for the user's selection.
```
</details>


## Flowcharts

<details>
  <summary>The Game Flow</summary>

  ![The Whole Game Flow](/media/game-flow.png)
</details>

<details>
  <summary>Play Flow</summary>

  ![Play Process Flow](/media/play-flow.png)
</details>

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>


# Used Technologies

## Python
  - Python programming language is the main component for developing this game.
  - Developed and tested on python version 3.8.11. 

### Modules and Packages

  - **Firebase Admin and Firestore**: connect Python code with the Firestore database.
  - **Bcrypt**: secure storage and retrieval of hashed and unhashed passwords.
  - **GetPass**: conceal the characters of passwords entered.
  - **Rich**: build tables and print markdown-formatted strings.
  - **Termcolor**: colour and manipulate text styles.
  - **Unittest**: create automated test classes.
  - **Typing union**: used to describe methods with multiple possible types of return.
  - **Random**: generate a random number.
  - **Time**: pause the game for a set amount of time.
  - **Signal**: change the behaviour of the CTRL+C keyboard input. 


## Other Softwares and Tools
  - **Google Firestore** is used to store and get the players' account data.
  - **Lucidchart** to design the game flowcharts.
  - **Gitpod** and **VS Code** for code development and testing.
  - **Heroku** for deploying the live version of this game.
  - **Github** is used for version control.
  - **Grammarly** and **QuillBot** to detect typos and grammatical errors.
  - **Node.js**, **HTML**, **CSS**, and **XTERM** to create the game's infrastructure layer. 

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>


# Features 

### Existing Features

- __Menus__

  - Game menus will allow the user to easily navigate all of the game's features by simply entering the number of the option he wants to select.
  - *Covered User stories: 5,6*
  - <details><summary>Main Menu Screenshot</summary>
      
      ![Main Menu](/media/main-menu-screen.PNG)
    </details>


- __Signup__

  - To play the game, first-time users must sign up by providing their name, email address, and password, as well as a confirmation password.
  - *Covered User stories: 7*
  - <details>
      <summary>Signup Screenshot</summary>

      ![Signup](/media/signup-screen.PNG)
    </details>


- __Login__

  - Existing users will be able to use their email and password to get into the game.
  - Authentication process is done on each login to check if the user has the right to access the game.
  Upon successful authentication, a greeting message will be printed.
  - *Covered User stories: 3, 8*
  - <details>
      <summary>Login Screenshot</summary>

      ![Login](/media/login-screen.PNG)
    </details>


- __Game Rules__

  - A text block that explains how the game works and how to play it to the user.
  - *Covered User stories: 1, 9*
  - <details>
      <summary>Rules Screenshot</summary>
      
      ![Rules](/media/rules-screen.PNG)
    </details>


- __About Game__

  - A text block containing information about the game and the developer.
  - *Covered User stories: 9*
  - <details>
      <summary>About Screenshot</summary>

      ![About](/media/about-screen.PNG)
    </details>


- __Levels__

  - level options are available to provide various difficulty levels.
  - Each level has its own board dimensions (rows and columns) and specific number of mines.
  - *Covered User stories: 2*
  - <details>
      <summary>Level Screenshot</summary>

      ![Level](/media/level-screen.PNG)
    </details>


- __Board__
  - Game board is shown in a coloured table style, the board mines' positions generated randomly.
  - Assists the user in determining mine position by providing the number of the neighbouring mine.
  - When the player loses, a real board with mines is displayed to inform the user of his incorrect cell choice.
  - *Covered User stories: 4, 5*
  - <details>
      <summary>Board Screenshot</summary>
      
      ![Board](/media/board-screen.PNG)
    </details>


- __Symbols and Colours__
  - Unrevealed cells' content is (?) to indicate that it's available for the user's choice.
  - Mines are in the form of red starred (*) shapes.
  - The colour of neighbouring mine cells indicates their danger level (red indicates very dangerous, orange indicates dangerous, and green indicates no mines).
  - *Covered User stories: 3, 5*
  - <details>
      <summary>Symbols and Colours Screenshot</summary>
      ![Symbols and Colours](/media/symbol-and-colour-screen.PNG)
    </details>


- __Feedback Messages__
  - Invalid user input triggers an appropriate message depending on the requested data.
  - Each user's coordination input is shown on the terminal to help the player track his moves.
  - To make it easier for the user to capture success messages, error messages are printed in red and success messages in green.
  - *Covered User stories: 3, 4, 5*
  - <details>
      <summary>Feedback Messages Screenshots</summary>
      
      ![Error](/media/feedback-1-screen.PNG)
      
      ![Coordination Input](/media/feedback-2-screen.PNG)
      
      ![Success](/media/feedback-3-screen.PNG)
    </details>

### Features Left to Implement

- Build a graphical user interface using [Textual framework](https://textual.textualize.io/).


<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>


# Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


## Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

## Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

# Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


# Credits 

- Flowcharts built with the help of [Stuff Made Easy Youtube channel](https://www.youtube.com/watch?v=Yq1OPs5hCt0&t=10s) and designed on [Lucidcharts](https://lucid.app/).

- Calling method from a string is a solution on Stackoverflow by [Sam Dolan](https://stackoverflow.com/questions/7936572/python-call-a-function-from-string-name)

- Rich python module used based on posts of [Ashutosh Krishna](https://www.freecodecamp.org/news/use-the-rich-library-in-python/) and [Martín Lamas](https://medium.com/trabe/building-rich-console-interfaces-in-python-16338cc30eaa).

- Big titles and fonts are a result of using pyfiglet python module described by [Khuyen Tran](https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b) post and [pyfiglet fonts](http://www.figlet.org/examples.html)

- Connecting Google Firestore with the Python code is inspired by [Anurag Sharma](https://faun.pub/getting-started-with-firebase-cloud-firestore-using-python-c6ab3f5ecae0) post.

- Hiding password characters in a user's input is a solution provided by [Have a nice day](https://stackoverflow.com/questions/66989546/hide-input-password-when-typing-in-python) on Stackoverflow.

- Email validation code using regular expressions is taken from this [Rohit Gupta](https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/) post.

- Based on [IDOWU OMISOLA] (https://www.makeuseof.com/encrypt-password-in-python-bcrypt/), Bcrypt is used for password hashing and hashed password comparison.

- Writing unit tests followed tutorials posted by [Bala Priya C](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/) and the [geertjanvdk's](https://stackoverflow.com/questions/17657543/python-unittest-setup-function) Stackoverflow solution.

- Mocking user input inside a unit test is an idea from [Pavel Vergeev](https://dev.to/vergeev/how-to-test-input-processing-in-python-3) blog.

- Writing typing hints for a function with multiple possible types of return is taken from [Bhargav Rao's] (https://stackoverflow.com/questions/33945261/how-to-specify-multiple-return-types-using-type-hints) Stackoverflow solution.

- Rich colours used in this game are brought from the [Colours List](https://rich.readthedocs.io/en/stable/appendix/colors.html).

- This readme file is based on the [Code Institute Readme Template](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md).

- Grammatical errors and typos on this file were discovered and corrected by [Grammarly](https://app.grammarly.com/) and [Quillbot](https://quillbot.com/grammar-check).

- Special thanks to my mentor, Mr. Mo Shami, for his continuous guidance and support.