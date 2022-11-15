<kbd>![Minesweeper](/media/logo.PNG)</kbd>

Developer: [Khubab Shamsuddin](https://www.linkedin.com/in/kshamse/)

Live Website: [Minesweeper](https://cli-minesweeper.herokuapp.com/)

![Main Screen](/media/main-screen.PNG)


# Table of Contents

- [Table of contents](#table-of-contents)
- [About Minesweeper](#about-minesweeper)
- [Goals](#goals)
  - [User's Goals](#users-goals)
  - [Owner's Goals](#owners-goals)
- [User Stories](#user-stories)
    - [User's Stories](#users-stories)
    - [Site's Owner Stories](#sites-owner-stories)
- [Game Design](#flowcharts-design)
  - [Pseudocode](#pseudocode)
  - [Flowcharts](#flowcharts)
- [Used Technologies](#used-technologies)
  - [Python](#python)
    - [Modules & Packages](#modules-and-packages)
  - [Firestore DB](#firestore)
  - [Other Softwares & Tools](#other-softwares-and-tools)
- [Features](#features)
  - [Menus](#menus)
  - [Signup](#signup)
  - [Login](#login)
  - [Game Rules](#game-rules)
  - [About Game](#about-game)
  - [Levels](#levels)
  - [Board](#board)
  - [Symbols and Colors](#symbols-and-colors)
  - [Feedback Messages](#feedback)
- [Validation](#validation)
- [Testing](#testing)
  - [Manual](#manual-testing)
  - [Automated](#automated-testing)
- [Bugs](#interesting-bugs)
- [Deployment](#deployment)
- [Credits](#credits)


# About Minesweeper

Minesweeper is a game designed to entertain Internet users. The game board is made up of many columns and rows, and the player must guess and calculate in order to reveal all cells that do not contain mines. The current game is command-line-based, which receives player-guessed cell coordination as input and checks if it has a mine or not. When all cells are revealed, the player wins; if a cell contains a mine, the player loses.

<a href="#love-running" title="Back to top"><img src="media/top.png" width="30" height="30"></a>

# Goals

## User's Goal

- Play an interesting logic game.

## Site Owner's Goal

- Build an interactive command-line version of the well-known minesweeper game.
- The game should provide amusement and joy to attract more users.

<a href="#love-running" title="Back to top"><img src="media/top.png" width="30" height="30"></a>

# User Stories

## User's Stories

1. I want to understand the game's rules.
2. I want to be able to control the game's difficulty.
3. I want to get clear feedback on my inputs.
4. I want to be able to review my choices.

## Site's Owner Stories

5. I want the game to be simple and clear.
6. I want the game to have a smooth and natural flow.
7. I want new users to be able to create a new account.
8. I want active users to be able to login to an existing account.
9. I want players to see information about the game and its rules.

# Game Design

## Pseudocode

<details>
  <summary>The Process Steps</summary>

```
1. Display the greeting message.

2. Inquiring about the user's account and providing the options "log in" and "sign up."
    - (2.1) If the user enters "1" for login, he will be asked to enter his email and password.
    - (2.2) If the user enters "2" signup, he will be asked to enter his name, email address, and password with confirmation, and a record will be created as a result.
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


## Features 

In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### Existing Features

- __Navigation Bar__

  - Featured on all three pages, the full responsive navigation bar includes links to the Logo, Home page, Gallery and Sign Up page and is identical in each page to allow for easy navigation.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png)

- __The landing page image__

  - The landing includes a photograph with text overlay to allow the user to see exactly which location this site would be applicable to. 
  - This section introduces the user to Love Running with an eye catching animation to grab their attention

<a href="#love-running" title="Back to top"><img src="media/top.png" width="30" height="30"></a>
<!-- [(![Landing Page](/media/top.png))](#love-running) -->
- __Club Ethos Section__

  - The club ethos section will allow the user to see the benefits of joining the Love Running meetups, as well as the benefits of running overall. 
  - This user will see the value of signing up for the Love Running meetups. This should encourage the user to consider running as their form of exercise. 

![Club Ethos](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png)

- __Meetup Times section__

  - This section will allow the user to see exactly when the meetups will happen, where they will be located and how long the run will be in kilometers. 
  - This section will be updated as these times change to keep the user up to date. 

![Meetup Times](https://github.com/lucyrush/readme-template/blob/master/media/love_running_times.png)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Love Running. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media

![Footer](https://github.com/lucyrush/readme-template/blob/master/media/love_running_footer.png)

- __Gallery__

  - The gallery will provide the user with supporting images to see what the meet ups look like. 
  - This section is valuable to the user as they will be able to easily identify the types of events the organisation puts together. 

![Gallery](https://github.com/lucyrush/readme-template/blob/master/media/love_running_gallery.png)

- __The Sign Up Page__

  - This page will allow the user to get signed up to Love Running to start their running journey with the community. The user will be able specify if they would like to take part in road, trail or both types of running. The user will be asked to submit their full name and email address. 

![Sign Up](https://github.com/lucyrush/readme-template/blob/master/media/love_running_signup.png)

For some/all of your features, you may choose to reference the specific project files that implement them.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement

- Another feature idea

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 