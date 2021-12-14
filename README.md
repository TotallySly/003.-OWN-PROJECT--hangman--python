# Hangman

This is a small project written in Python. It is the classic game of Hangman. It is a simple word guessing game in which the user guesses the mystery word, letter-by-letter.

About Hangman -  [Hangman Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

Link to the project -  [Hangman - The Game](https://game-of-hang-the-man.herokuapp.com/)

![Responsive Mockup](assets/read_me_images/responsive_mockup.png)

***

## Table of Contents
  * [UX and UI Design](#ux-and-ui-design)
    * [Owner Goals](#owner-goals)
    * [User Goals](#user-goals)
    * [Potential Features to Use](#potential-features-to-use)
    * [Wireframes](#wireframes)
    * [Flow Chart](#flowchart)
  * [Design](#design)
    * [Imagery](#imagery)
  * [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left To Implement](#features-left-to-implement)
    * [Technologies Used](#technologies-used)
  * [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Manual Testing](#manual-testing)
    * [Bugs](#unfixed-bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgments](#acknowledgements)

***

## UX and UI Design

UX and UI Design is limited due to the catch all design for terminal based projects. 

*** 

### Owner Goals

- To deploy a working game of Hangman that validates user input.
- To create a slight variation of the game. To allow for different degrees of difficulty.
- To challenge the user.


***

### User Goals

- Understand the game with ease.
- Option to chose the level of difficulty level of the game.
- Easy to user and navigate.

***


### Wireframes

Due to the game being played within the terminal, I did not use any design wireframes as the design is restricted to that of the terminal.

***

### Flowchart

FLOWCHART LOGIC

***

## Design

### Imagery

I used ASCII Art as the imagery within this project.

[ASCII Art Wikipedia](https://en.wikipedia.org/wiki/ASCII_art)

***

## Features

### Existing Features

#### Logo
  
  - The Logo is the word Hangman designed in ASCII Art

![Logo](assets/readme-images/logo.png)
 
 ***

#### Menu
  
  - The Menu is loaded, with the logo, in the terminal.
  - It asks the user if they would like to the play the game or not.

![Menu](assets/readme-images/menu.png)

***

#### End Game

 - If the user chooses not to play the game. Then we say goodbye to the user and the game will end.


![End Game](assets/readme-images/endgame.png)

***

#### Play Game

  - If the user chose to play the game, they are then asked if they would like to play with three, four, or a five lettered word.
  - The size of the word is repeated to the user.
  - Then the game begins, asking the user to guess a letter.

![Play Game](/assets/readme-images/playgame.png)

***

#### In Game Play (Incorrect)

  - After the user makes inputs a guess, a list of guessed letters is shown to the user. This allows the user to see which letters they have guessed throughout the game. This is displayed with the letter is NOT in the word.

  - The amount of lives left is displayed.

  - The ASCII Art is displayed showcasing the stage of life the user is at.  

![In Game Play](assets/readme-images/ingame.png)


***

#### In Game Play (Correct)

  - The word is displayed to the user, with the correct letter displayed in the correct position, to the user.
  - The amount of lives are still displayed to the user.
  - The ASCII Art of the stages of Hangman are displayed.
  - A list of guessed letters is still displayed to the user.
  - Asks the User to guess the letter.

![Prices](assets/readme-images/ingame-correct.png)

***

#### Win Game

- If the winner correctly guesses all the letters, "You Win" is displayed to the user.
- The user is asked if they would like to play again.
- If yes, the loop of the game starts again, or it ends if the user inputs no. 

![Win Game](assets/readme-images/wingame.png)


***

#### Lose Game

  - If the user loses the game, they are asked if they would like to play again. If yes, the loop will start again. If not, the game will end.

![Lose Game](assets/readme-images/losegame.png)

***

#### User Validation One

  - User Validation 1. If the User inputs anything OTHER than "Y" or "N" then an invalid response is displayed to the user, and they are asked to input again.

![User Validation One](assets/readme-images/valid1.png)

***

#### User Validation Two

  - User Validation 2. If the User inputs anything OTHER than "3", "4", or "5" then an invalid response is displayed to the user, and they are asked to input again.

![User Validation Two](assets/readme-images/valid2.png)
  
***

#### User Validation Three

  - User Validation Three. If the user inputs anythin after than a letter, then the lives are displayed to the user, stating a life has not been taken away.
  - The Iser is told that the input is invalid, and would they guess again.

![User Validation Three](assets/readme-images/valid3.png)
  
***

#### Features Left To Implement

  - More sized words! I had a time constraint due to having three weeks to learn Python for this hand-in. If I had more time I would have words varying in different sizes, maybe going up to 10. Allowing for different difficulties.
  - Random word feature. Am additional list where I take all different sized words to produce a more 'traditional' hangman game.
  - Scoreboard. If the user would like to keep playing, allowing a high score feature? Or a score feature that gives higher points the quicker you guess the word.

## Technologies Used

Languages
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Technologies Used

  - [GitPod](https://gitpod.io/)
    - The online IDE was used to write the code and testing within the terminal.
  - [Git](https://git-scm.com/)
    - Was used for version control.
  - [GitHub](https://github.com/)
    - As a repository and storing the projects code.
  - [Heroku](https://www.heroku.com/home)
    - Used as deployment for the game.
  - [Lucidchart](https://www.lucidchart.com/pages/)
    - To produce the flowchart of the game's logic.
  
Frameworks and Libraries
 - [Code Institute - Template](https://github.com/Code-Institute-Org/gitpod-full-template)
 - All Python Modules used were the internal Python Libraries/Modules. These were the Random and String Module. 

***

## Testing

### Validator Testing

![PEP8 - Online Check](assets/readme-images/validator.png)


***

### Manual Testing

The site was manually tested throughout production. Every function, or additional line of code was printed to the terminal to check if the code was running correctly.

I asked several people to be 'beta' testers, who tried their best to completely break the game. I used people who do not code as I believe these people are always the best to test projects on.

***

### Bugs


## Deployment
  
  - The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
    - From the source section drop-down menu, select the Master Branch
    - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

- The link:
  - [The English Football Club - Website](https://totallysly.github.io/portfolio-project-one/)

***

## Credits
  
### Content

  All written content is purely fictional. I created the written content myself as the company is also fictional. 
  - The training section was inspired by a section of tutorial project, [Love Running](https://github.com/Code-Institute-Solutions/love-running-2.0-sourcecode/tree/main/05-meetup-times), via the Code Institute.
  - A lot of research was placed on [Stack Overflow](https://stackoverflow.com/), [W3Schools](https://www.w3schools.com/), [Mozilla Developer](https://developer.mozilla.org/en-US/)
  - I implemented a 'Scroll to Top Button' - [Scroll to Top Button](https://www.youtube.com/watch?v=Vef9bxTilCU&ab_channel=DarkCode)
  - Help with Code for the form [Form Code](https://dev.to/uma/responsive-form-using-html-and-css-4l59)
  - [Position Absolute and Relative](https://thoughtbot.com/blog/positioning#position)
  -  [CSS Tricks Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox)
  -  [Which CSS Units to Use?](https://gist.github.com/basham/2175a16ab7c60ce8e001)
  -  [Responsive Google Maps](https://blog.duda.co/responsive-google-maps-for-your-website)
  -  [Media Queries](https://stackoverflow.com/questions/6370690/media-queries-how-to-target-desktop-tablet-and-mobile)
  - In addition several YouTube videos:
      - [Web Dev Simplified](https://www.youtube.com/c/WebDevSimplified/playlists) (Flexbox, Absolute/Relative Position).
      - [Kevin Powell](https://www.youtube.com/kepowob). (Flexbox, Absolute/Relative Position)
      - [Minim](https://www.youtube.com/watch?v=VX_Dghv65Vk&list=PL4cTxE4s2XIYJL6uPQUwMt25M70gPl-O6&index=14&ab_channel=Minim). (Sign-Up form).
  - The README Template was a mix of Code Institute's README Template for [Love Running](https://github.com/Code-Institute-Solutions/readme-template) and the excellent website and README by [Aofie Smith](https://github.com/aoifesmith/evanandanna/blob/main/README.md)

  - Icons where via the amazing website - [Font Awesome](https://fontawesome.com/).
  - The colour palette was from [Coolors](https://coolors.co/)
  - Additional Responsive Tool [Responsive PX](http://www.responsivepx.com/)
  - And of course, Google Dev Tools.

***

### Media

  - My images were from two stock image websites: [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/).


 - Hero Image [Pixabay](https://www.pexels.com/@pixabay)
 - Coaches Background Image [Ralph (Ravi) Kayden](https://unsplash.com/@ralphkayden?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
- Coach Richards Image [Midas Hofstra](https://unsplash.com/@midashofstra)
- Coach Edwards Image [Ben Den Engelsen](https://unsplash.com/@benjeeeman)
- Training Times Image [Mike](https://www.pexels.com/@mike-468229)
- Sign-Up Background Image [Kampus](https://www.pexels.com/@kampus)
  
***

### Acknowledgements

I would like to thank my Code Institute mentor Antonija Simic for her help and guidance during this project.

I would like to thank the Code Institute Slack community for all their support and help with various general questions I have asked thus far. Specifically to David_Bowers5p and Aoife Smith_5p for their Peer-Code-Review feedback, and Eventyret_Mentor for answering a lot of my questions. 

***