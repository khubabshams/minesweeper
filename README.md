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
- [User Manual](#user-manual)
- [Game Design](#game-design)
  - [Pseudocode](#pseudocode)
  - [Flowcharts](#flowcharts)
  - [Data Models](#data-models)
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
- [Testing](#testing)
  - [Manual](#manual-testing)
  - [Automated](#automated-testing)
  - [Validator](#validator-testing)
  - [Bugs](#interesting-bugs)
- [Deployment](#deployment)
- [Credits](#credits)


# About Minesweeper

Minesweeper is a game designed to entertain Internet users. The game board is made up of many columns and rows, and the player must guess and calculate in order to reveal all cells that do not contain mines. The current game is command-line-based, which receives player-guessed cell coordination as input and checks if it has a mine or not. When all cells are revealed, the player wins; if a cell contains a mine, the player loses.

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>

# Goals

## User's Goals

- Play an interesting logic game.
- Understands how the game works.
- Be able login with a registered account.

## Site Owner's Goals

- Build an interactive command-line version of the well-known minesweeper game.
- The game should provide amusement and joy to attract more users.
- Promote owner's information and the game description.

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

# User Manual

<details>
  <summary>Click here to see instructions.</summary>

__Account Menu__
  
When the game starts and after the greeting message, the account menu (have account?) appears with two options:
1. Yes, we will ask you to sign in
2. No, you can signup to have one
Operation: Enter the number of the selected option.

__Login__

When the user selects the first option in the account menu, login data will be requested.
Operation: Enter email, then password.
A message will show up to inform the user of the login process status; if login fails, the user will be asked to enter his credentials again.

__Sign Up__

If the user selects the second choice of the account menu, he will be asked to fill out signup data.
Operation: Enter name, email, password, and confirms his password.
Name, email, and password must start with a letter, not a number.
Email must be formatted as email@provider.com, net, etc.
Passwords must be at least eight characters long.

__Main Menu__

Once user logged in, main menu appears with three options shown:
1. Start Game
2. Rules
3. About
Operation: Enter a number in the options range.
When the user selects Rules or About, a related text block will be shown, and after a while, the main menu will appear again.

__Level Menu__

When the user selects the first option in the main menu, he will be asked to choose the level of the game.
1. Easy 3x3 (3 Mines)
2. Medium 4x4 (6 Mines)
3. Hard 6x6 (16 Mines)
Each level has a different board size and number of mines, as mentioned.

__Game Round__

Once the round has begun, the board will be displayed, followed by a request for the row and column of the user's guess.
Operation: Enter a row number from zero to the maximum row number on the board, then enter a column number (the same rule applies).
User mustn't enter a cell position which entered before.
If selected cell has a mine user will be informed and game will be ended, otherwise the board will be shown and neighbouring mines number of the selected cell will appear inside it.
Round will be repeated until the player reveal all cells successfully.

__Play Again Menu__

When the game ends, the player will be asked if he would like to play again.
1. Yes
2. No
Operation: Enter the selected option number.
If you answer yes, a game of the same level will begin; otherwise, the main menu will appear.

__Note__

At any time the user enters an invalid input or an unfound option number, feedback will be prompted and the user will be requested to repeat the operation.
</details>

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

## Data Models

- The game code was written following object-oriented programming principles.

  <details>
    <summary>Data Models Details</summary>

    - **Classes** Four classes have been written: (Board, User, Game, and UtilityMixin), the last one is a mixin that contains functions such as styled print functions. All other classes inherited the mixin in order to reuse its common functionalities.
    - **Unit Tests** Each Python class in the above list has its own unit testing class to test its main methods.
  </details>


# Used Technologies

## Python
  - Python programming language is the main component for developing this game.
  - Developed and tested on python version 3.8.11.

### Modules and Packages

__Built-in__
  - **Random** generate a random number.
  - **Time** pauses the game for a set amount of time.
  - **Signal** change the behaviour of the CTRL+C keyboard input. 
  - **Rich** build tables and print markdown-formatted strings.
  - **Unittest** create automated test classes.
  - **Typing union** describes methods with multiple possible types of return.

__3rd Party__
  - **Firebase Admin and Firestore**: I used these to connect Python code with the Firestore database.
  - **Bcrypt**: I used Bcrypt to store and retrieve hashed and unhashed passwords securely.
  - **GetPass**: I used it to conceal the characters of passwords entered by the user.
  - **Termcolor**: I used this to colour and change the style of text.
  - **pycodestyle**: I used it to validate Python code and ensure that it adhered to conventions.


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

#### Menus

  - Game menus will allow the user to easily navigate all of the game's features by simply entering the number of the option he wants to select.
  - *Covered User stories: 5,6*
  - <details><summary>Main Menu Screenshot</summary>
      
      ![Main Menu](/media/main-menu-screen.PNG)
    </details>


#### Signup

  - To play the game, first-time users must sign up by providing their name, email address, and password, as well as a confirmation password.
  - *Covered User stories: 7*
  - <details>
      <summary>Signup Screenshot</summary>

      ![Signup](/media/signup-screen.PNG)
    </details>


#### Login

  - Existing users will be able to use their email and password to get into the game.
  - Authentication process is done on each login to check if the user has the right to access the game.
  Upon successful authentication, a greeting message will be printed.
  - *Covered User stories: 3, 8*
  - <details>
      <summary>Login Screenshot</summary>

      ![Login](/media/login-screen.PNG)
    </details>


#### Game Rules

  - A text block that explains how the game works and how to play it to the user.
  - *Covered User stories: 1, 9*
  - <details>
      <summary>Rules Screenshot</summary>
      
      ![Rules](/media/rules-screen.PNG)
    </details>


#### About Game

  - A text block containing information about the game and the developer.
  - *Covered User stories: 9*
  - <details>
      <summary>About Screenshot</summary>

      ![About](/media/about-screen.PNG)
    </details>


#### Levels

  - level options are available to provide various difficulty levels.
  - Each level has its own board dimensions (rows and columns) and specific number of mines.
  - *Covered User stories: 2*
  - <details>
      <summary>Level Screenshot</summary>

      ![Level](/media/level-screen.PNG)
    </details>


#### Board

  - Game board is shown in a coloured table style, the board mines' positions generated randomly.
  - Assists the user in determining mine position by providing the number of the neighbouring mine.
  - When the player loses, a real board with mines is displayed to inform the user of his incorrect cell choice.
  - *Covered User stories: 4, 5*
  - <details>
      <summary>Board Screenshot</summary>
      
      ![Board](/media/board-screen.PNG)
    </details>


#### Symbols and Colours

  - Unrevealed cells' content is (?) to indicate that it's available for the user's choice.
  - Mines are in the form of red starred (*) shapes.
  - The colour of neighbouring mine cells indicates their danger level (red indicates very dangerous, orange indicates dangerous, and green indicates no mines).
  - *Covered User stories: 3, 5*
  - <details>
      <summary>Symbols and Colours Screenshot</summary>
      ![Symbols and Colours](/media/symbol-and-colour-screen.PNG)
    </details>


 #### Feedback Messages

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

## Manual Testing

  <details>
    <summary>User Stories Testing</summary>

  1. I want to understand the game's rules
  
  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Main menu -> Rules | Select option 2 | The rules of the game are presented to the user | Performs as expected |


  2. I want to be able to control the game's difficulty.
  
  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Main Menu -> Start Game| Select option 1 | The user will be asked to select the game level | Performs as expected |

  3. I want to get clear feedback on my inputs.

  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Across the game | Valid/ invalid input | The user will see the response to his input, whether it's a message or a menu | Performs as expected |

  4. I want to be able to review my choices.

  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Across the game | Valid/ invalid input | The user will be able to scroll and review his previous options | Performs as expected |

  5. I want the game to be simple and clear.
  
  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Menus | Select option number | The user will be asked to enter only selected option's number | Performs as expected |
  | Board | - | The text is coloured and symbols are used to make the data on the board easier to read | Performs as expected |
  
  6. I want the game to have a smooth and natural flow.

  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Across the game | - | The user is guided through simple instructions and nested options in a circular motion | Performs as expected |

  7. I want new users to be able to create a new account.
  
  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Account Menu -> No (Signup) | Select option 2 | Users are able to signup using un-registered emails | Performs as expected |

  8. I want active users to be able to login to an existing account.
  
  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Account Menu -> Yes (Login) | Select option 1 | Users can log in using their email addresses and passwords | Performs as expected |

  9. I want players to see information about the game and its rules.

  | **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
  | ------------- | ----------------------------- | ---------------------------- | ----------------- |
  | Main Menu -> Rules | Select option 2 | Users will see the game rules | Performs as expected |
  | Main Menu -> About | Select option 3 | Users will see information about the game and the developer | Performs as expected |


  </details>

## Automated Testing

- Unit test classes have been written to test the functionalities of the Minesweeper game.
- The CLI command to run the tests with the print statements buffered is:

  `python3 test.py -b`

- Test results:
  <details>
    <summary>All tests passed successfully</summary>

    ![Unittests Result](/media/unittests-result.PNG)
  </details>


## Validator Testing 

- The game code has passed the `pycodestyle` linter validations with no errors or warnings shown.
- I applied a filter `**/*.py` on VSCode to show only problems within all Python files.
- Validatior Results:
  <details>
    <summary>No problem was detected by the linter</summary>

    ![Pycodestyle Result](/media/pycodestyle-linter-result.PNG)
  </details>

## Interesting Bugs

### List Update 

- **Bug**: updating an index of the cells 2-d list will affect that all similar index updated with the same value.
- **Debugging**: found the problem in list creation, I create the one list of row then multiply it by the number of rows and so for the columns which cause <u>Passing the same created list reference</u> for the rest of lists.
- **Solution**: replace the code of list creation
`return [[0] * self.col_size] * self.row_size` 
With 
`[['?' for col in range(self.col_size)] for row in range(self.row_size)]`.


### Test Running 

- **Bug**: importing `run.py` inside `test.py` file runs the game.
- **Debugging**: Based on [this Stackoverflow answer](https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it) I found that I <u>have to start game when the `__name__` attribute value is `__main__`</u> in order to prevent the code from being executed on import statement calls.
- **Solution**: wrap the code of game starting
```game = Game() game.run()```
Inside the condition
`if __name__ == '__main__':`.


### Rich Not Found 

- **Bug**: on the deployed version on `Heroku` I got an error `ModuleNotFoundError: No module named 'rich'` even it's working as a charm on local machine.
- **Debugging**: I've looked in requirements.txt I found that rich isn't generated by the `pip3 freeze` command; because it's considered as a built in module probably, I tried `python3 -m pip check` to find missing dependencies on local but I got `No broken requirements found`.
- **Solution**: I added `rich==12.4.4` manually to the requirements.txt after looking on [the issue](https://github.com/elebumm/RedditVideoMakerBot/issues/60) referred by GaMiNgEr9978 user on `Github`.


### Rich Tables with Emojis and PyFiglet Fonts
- **Bug**: broken text style when using the deployed version but working fine on local.
- **Debugging**: I tried to change terminal column size but it was still the same, for tables I noticed that cells with number in it printed with required shape but the ones with emojis crashes and pyfiglet text not works on deployed version as well.
- **Solution**: I replaced emojis with symbols and copied the text content from the local machine of pyfiglet and added the copied text to print statements.


<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>


# Deployment

## How to Deploy

- The site was deployed to `Heroku`. The steps to deployment are as follows:
  <details>
    <summary>Click here to see related deployment instructions</summary>

    - After you've signed up, navigate to the [Heroku apps page](https://dashboard.heroku.com/apps) and click `Create New App.`
    - Enter the application name and the region, then click on `Create App`.
    - Once the app has been created, go to the `Settings` tab.
    - In settings, click on `Reveal Config Vars` and set the case-sensitive word `CREDS` to the `KEY` field, then copy all of your credentials json file content into the `VALUE` area and click on the `Add` button.
    - Next, select `Add buildback` Select `python` as the first buildpack and click `Save changes` then do the same for `node.js`, Following the given sequence is very important.
    - Once the settings are complete, navigate to the `Deploy` tab.
    - Select `Github` from the `Deployment method` options.
    - Connect your `Heroku` account with `Github` and grant Heroku` the required authorization.
    - Find the name of the repository that you want to deploy.
    - Click `Connect` on the wanted `repo` and select the branch from the `Choose a branch to deploy` dropdown button.
    - Choose `Automatic deploys` to automatically deploy the application whenever code has been pushed to the selected branch (You recommended having a CI service configured on the repo).
    - OR
    - When the `Deploy Branch` button is clicked, select `Manual Deploy` to deploy the branch.
    - Review the deployment debugger output if there's a deployment issue.
    - When the deployment is complete, you'll see the message `Your app was successfully deployed` and you can open your application page by clicking the `View` button.

    
    - The live link can be found here: https://cli-minesweeper.herokuapp.com/

  </details>


## How to Make a Local Clone

- To clone this repository to your local machine:

  <details>
    <summary>Click to see related deployment instructions</summary>

    - From [Minesweeper Github](https://github.com/kshamse/minesweeper) click on `<> Code` drop-down button and select the suitable clone option.
    - Click on the `HTTPS` or `SSH` (requires an SSH key to be configured on your machine) tab and copy the URL.
    - Open your terminal or `Git` bash window and change the directory to where you want to clone.
    - Enter the following command, but don't forget to replace the `<copied URL>`:

      `git clone <copied URL>`
    
    - The same-named directory will be downloaded to the clone path.
  </details>

## How to Fork this Repository

- To fork this repository, please follow the below steps:

  <details>
    <summary>Click to see related deployment instructions</summary>

    - If you're not seeing this on Github`, click on [this link](https://github.com/kshamse/minesweeper) to open up the repository.
    - On the top right side of this page, click on `Fork`.
    - Change the forked repository if you want to, and you can add a description as well.
    - Leave the branch option `Copy the main branch only` checked.
    - Click on `Create Fork` to complete forking.
  </details>

<a href="#table-of-contents" title="Back to top"><img src="media/top.png" width="30" height="30"></a>


# Credits 

- Flowcharts built with the help of [Stuff Made Easy Youtube channel](https://www.youtube.com/watch?v=Yq1OPs5hCt0&t=10s) and designed on [Lucidcharts](https://lucid.app/).

- Calling method from a string is a solution on Stackoverflow by [Sam Dolan](https://stackoverflow.com/questions/7936572/python-call-a-function-from-string-name)

- Rich python module used based on posts of [Ashutosh Krishna](https://www.freecodecamp.org/news/use-the-rich-library-in-python/) and [Martín Lamas](https://medium.com/trabe/building-rich-console-interfaces-in-python-16338cc30eaa).

- Big titles and fonts are a result of using pyfiglet python module described by [Khuyen Tran](https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b) post and [pyfiglet fonts](http://www.figlet.org/examples.html)

- Connecting Google Firestore with the Python code is inspired by [Anurag Sharma](https://faun.pub/getting-started-with-firebase-cloud-firestore-using-python-c6ab3f5ecae0) post.

- Hiding password characters in a user's input is a solution provided by [Have a nice day](https://stackoverflow.com/questions/66989546/hide-input-password-when-typing-in-python) on Stackoverflow.

- Email validation code using regular expressions is taken from this [Rohit Gupta](https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/) post.

- Based on [IDOWU OMISOLA](https://www.makeuseof.com/encrypt-password-in-python-bcrypt/), Bcrypt is used for password hashing and hashed password comparison.

- Writing unit tests followed tutorials posted by [Bala Priya C](https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/) and the [geertjanvdk's](https://stackoverflow.com/questions/17657543/python-unittest-setup-function) Stackoverflow solution.

- Mocking user input inside a unit test is an idea from [Pavel Vergeev](https://dev.to/vergeev/how-to-test-input-processing-in-python-3) blog.

- Writing typing hints for a function with multiple possible types of return is taken from [Bhargav Rao's](https://stackoverflow.com/questions/33945261/how-to-specify-multiple-return-types-using-type-hints) Stackoverflow solution.

- Rich colours used in this game are brought from the [Colours List](https://rich.readthedocs.io/en/stable/appendix/colors.html).

- This readme file is based on the [Code Institute Readme Template](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md).

- Grammatical errors and typos on this file were discovered and corrected by [Grammarly](https://app.grammarly.com/) and [Quillbot](https://quillbot.com/grammar-check).

- Special thanks to my mentor, Mr. Mo Shami, for his continuous guidance and support.