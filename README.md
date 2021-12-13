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
    * [Accessibility](#accessibility)
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

## Technologies Used

Languages
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  
Frameworks and Libraries
  - [Am I Responsive?](http://ami.responsivedesign.is/)
  - [GitBash](https://gitforwindows.org/)
  - [GitHub](https://github.com/)
  - [VS Code](https://code.visualstudio.com/)

***

## Testing

### Validator Testing

  HTML
    <details>
      <summary>'index.html' - Zero Errors</summary>
      ![index.html](assets/readme-images/w3schools-index-validator.png)
    </details>
    <details>
    <summary>'sign-up.html' - Zero Errors</summary>
    ![sign-up.html](assets/readme-images/w3schoold-sign-up-validator.png)
    </details>
        <details>
    <summary>'form-submit.html' - Zero Errors</summary>
    ![form-submit.html](assets/readme-images/w3schools-form-submit-validator.png)
    </details>
            <details>
    <summary>'404.html' - Zero Errors</summary>
    ![404.html](assets/readme-images/w3schoold-404-validator%20.png)
    </details>



  CSS
    <details>
      <summary>'styles.css' - Zero Errors</summary>
      ![styles.css](assets/readme-images/w3schools-css-validator.png)
    </details>
    <details>
      <summary>'styles.css' - 1 Warning</summary>
      ![One Warning](assets/readme-images/w3schools-css-warning.png)
    </details>

  This is due to importing Google Fonts onto the CSS stylesheet. The W3Schools Jigsaw Validator does not check imported style sheets.

***

### Manual Testing

The site was manually tested throughout production. This included ensuring 
   - All navigation links corresponded to the correct part of the website. 
   - The sign-up form had the necessary required attributes, ensuring all data needed was submitted.
     - The 'sign-up!' button directed to the correct page, telling the user that we had received their data.
   - A working Error 404 page, with a link directing the user back to the homepage.

Responsive testing was conducted on a Windows Laptop, iPhone 7, iPhone 7 plus, and a Samsung Galaxy Tab A8. As these devices are limited to their screen sizes. I also tested the responsiveness using Google Dev Tools and [Responsive PX](http://www.responsivepx.com/).

Testing was conducted on Google Chrome, Mozilla Firefox and Safari web browsers.

After website completion, I submitted the website to Code Institute's Slack Community, specifically the 'Peer-Code-Review' channel. 

***

### Accessibility

The website passes on all aspects of accessibility and colour contrast. 

Lighthouse Testing

  <details>
  <summary>'index.html' - Desktop</summary>

  ![index Desktop](assets/readme-images/lighthouse-index-desktop.png)
  </details>

  <details>
  <summary>'index.html' - Mobile</summary>

  ![index Mobile](assets/readme-images/lighthouse-index-mobile.png)
  </details>

  <details>
  <summary>'sign-up.html' - Desktop</summary>

  ![signup Desktop](assets/readme-images/lighthouse-signup-desktop.png)
  </details>

  <details>
  <summary>'sign-up.html' - Mobile</summary>

  ![signup Mobile](assets/readme-images/lighthouse-signup-mobile.png)
  </details>

  <details>
  <summary>'formsubmit.html' - Desktop</summary>

  ![formsubmit Desktop](assets/readme-images/lighthouse-formsubmit-desktop.png)
  </details>

  <details>
  <summary>'formsubmit.html' - Mobile</summary>

  ![formsubmit Mobile](assets/readme-images/lighthouse-formsubmit-mobile.png)
  </details>

  <details>
  <summary>'404.html' - Desktop</summary>

  ![404 Desktop](assets/readme-images/lighthouse-404-desktop.png)
  </details>

  <details>
  <summary>'404.html' - Mobile</summary>

  ![404 Mobile](assets/readme-images/lighthouse-404-mobile.png)
  </details>  

<br>
Wave

  <details>
  <summary>'index.html'</summary>

  ![index Mobile](assets/readme-images/wave-index.png)
  </details>

  <details>
  <summary>'sign-up.html'</summary>

  ![signup](assets/readme-images/wave-signup.png)
  </details> 

  <details>
  <summary>'form-submit.html'</summary>

  ![formsubmit](assets/readme-images/wave-formsubmit.png)
  </details>

  <details>
  <summary>'404.html'</summary>

  ![404](assets/readme-images/wave-404.png)
  </details>  
  
***

### Bugs

I had a lot of issues with the Sign-Up Form. It took me a long time to come to a final solution of having a fully responsive form for all media devices.

- Bug 1 - Hero Image
  I had issues with my original hero image. Due to context of the image, and the pixel size, it created an off-balance look. It overcome this, I opted for a different hero image. Upon speaking with the test users and owners, they agreed that the new hero image was better for the overall story of the website.

- Bug 2 - Coaches & Contact Us
  I had issues with the content for each coach. I solved this by using Flexbox. I also opted to remove the coaches' facts on mobile devices. This is so contact information is clearly seen by the user. 

 - Bug 2 - Sign-Up Form
  Position: Relative' and 'Position: Absolute'. For Desktop and Tablets there was no issue. However, on mobile devices, the sign-up form was off the page, or loading over the footer. I solved this issue by removing the background image and using a background colour instead. This also help to dramatically increase the performance of on mobile devices. I also made a smaller font-size, and managed to move the Position: Absolute toward the left side.

 - Bug 3 - Navigation Bar
  I had issues regarding the navigation bar for mobile devices. I used Flexbox in order to create the nav bar, however, on a mobile device it looked too 'busy' with messy ordering. I opted to change the nav bar to a column on mobile devices. This was a better representation. Using two different iPhones, I was able to use the links without any difficulty. This could be a future bug, as I note that it was the Nav bar that hindered my 100% scores to mid 90s on Lighthouse. Going forward, I would like to implement a 'Hamburger' Nav bar for Mobile devices. Upon research, JavaScript is required for this. After immersing myself into JavaScript, this bug will be corrected, and as such achieve 100% on Lighthouse.

- Bug 4 - W3Schools Validator
  After running my code through the validator. It returned several 'typos' within the code itself. This included:
    - Unclosed Divs.
    - Divs within the Fieldset and Legend
    - 'Di' being typed instead of Divs.

***

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