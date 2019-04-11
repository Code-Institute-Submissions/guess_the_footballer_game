# [Guess the Footballer Game](https://guess-the-footballer.herokuapp.com/)

This game has been developed for my Practical Python Milestone Project as part of the Code Institute’s Diploma in Full Stack Web Development course.

## UX

### User Stories

- Visitors to the website will need to understand how to play the game and see the rules.
- New players will need register so they can play the game.
- Returning users will need to login to play the game.
- Once the game has started, a clear image of the footballer is to be presented.
- Players will require to input their answer into a clearly shown input field and submit their answer.
- Players will require to see which question number they are on.
- Players will require to see if they have guessed correctly or incorrectly.
- Players will require to see their score as they progress playing the game
- Players will require to see when they have finished the game and what their final score was.
- Players will require to see where they rank on a scoreboard.
- Visitors may require to contact the game developer for their comments.

## Features

### Existing Features

1. The [index page](templates/index.html) states the rules of the game and how to play. Links are provided in the navbar to register, login or contact.
1. The [register page](templates/register.html) allows the user to register a username. Usernames must be unique and so are checked against the usernames stored in a file. If a username is already taken, the user is asked to choose a different username.
1. The [login page](templates/login.html) allows the user to login if they have already registered a username. If the username is not recognised, the user is asked to register to play the game.
1. Once the user either register's or log's in, the user is redirected to the [play game page](templates/play.html). A welcome message for the user is displayed in the navbar. A randomly shuffled image of a footballer is displayed from the [players file](data/players.json).
1. Once a user is logged in or registered a new navbar link is shown so that a user can logout and any time without completing the quiz. This will log the user out, end the user session and redirect back the the [index page](templates/index.html). If the user logs out before completing the quiz their score is not recorded and stored for the [scoreboard](templates/scoreboard.html). 
1. The [play game page](templates/play.html) loads the randomly shuffled player images into a jinja template where the player image and correct answer are inserted. The user then enters their answer in the field provided and clicks submit, upon which the next randomly generated player image will be shown as the next question.
1. Above the next question a message is displayed to state whether the previous question was answered correctly or not as well as displaying the users current score. The correct answer is in a hidden form field and compares the users answer to check if it is correct or not. The 
1. Once the user has completed 20 questions their final score will be displayed. A message is then shown to ask the user to check the [scoreboard](templates/scoreboard.html) scoreboard to see where they rank in the list of users. this can be via a link in the message text or through the navbar where a new link is displayed for users who complete the quiz to visit the scoreboard page. reached the last question, write their score to the [leaderboard file](data/scores.json) and redirect them to the [leaderboard page](templates/leaderboard.html).

## Technologies Used

The app was built using [Python](https://www.python.org/) code.

Other technologies used in this project are:

- [Flask](http://flask.pocoo.org/), a Python Microframework
  - for Flask sessions to store data temporarily
  - for routing
  - for redirecting and rendering templates
  - for displaying flash messages
  - for requesting methods
- [Jinja2](http://jinja.pocoo.org/docs/2.10/), a templating language
  - for rendering data in the html templates, communicating between front-end and back-end.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), the most basic building block of the Web
  - for writing the basic front-end content
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), a stylesheet language
  - for styling the page
- [JQuery](https://jquery.com)
  - for allowing the Javascript functionality in Bootstrap to work.
- [Bootstrap](http://getbootstrap.com/), a front-end framework
  - for general responsiveness.
  - for inegral components such as navbar and mobile friendly pages. 

## Testing

Manual testing has been performed to test the features of the Guess the Footballer Game.

The login feature has been tested by entering an unregistered user name into the login field. A message to inform the user that they are not registered is correctly displayed, as well as a message to inform the user if a username is already taken. Equally testing has been performed and validated for registered users to log in and for new users registering who are both taken directly to question 1 once they are logged in. Once the user logs in or registers a welcome message is displayed in the navbar, which manual testing has validated. The logout feature has been tested and correctly logs the user out and redirects back to the home page.

The contact and homepage links were tested to ensure they work correctly in the navbar.

A number of complete quizes have been performed answering all 20 questions. This has confirmed that the images of each footballer are being randomly generated as expected. During this testing both correct and incorrect answers were submitted to ensure these are validated and generating the correct score for each game. Question numbers and messages for correct and incorrect answers are both working correctly and have been validated by extensive testing. Once all 20 questions have been answered the correct final score is displaying correctly, with a message to go to the scoreboard to see where the user ranks on the all time list.

The scoreboard is correctly showing and ranking the users by their final score for the quiz. Each user is being added to the scorebaord upon answering the final question.

## Deployment

This app is hosted on Heroku. To be able to run the code on Heroku, a Procfile was added to tell Heroku it's a Python project (web: python app.py), as were the Config vars for IP (0.0.0.0) and PORT (5000).

## Credits
Jonathan Walters - This project was completed as part of Code Institute’s Diploma in Full Stack Web Development course in 2018.