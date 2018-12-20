# [Guess The Footballer Game] (https://guess-the-footballer.herokuapp.com/)

This game has been developed as part of my Full Stack Developer Diploma Practical Python Milestone Project.

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
- Players will require to see where they rank on a leaderboard.
- Visitors may require to contact the game developer for their comments.

## Features

### Existing Features

1. The [index page](templates/index.html) states the rules of the game and how to plays. Links are provided in the navbar to register, login or contact.
1. The [register page](templates/register.html) allows the user to register a username. Usernames must be unique so are checked against the usernames stored in a file. If a username is already taken, the user is asked to choose a different username.
1. The [login page](templates/login.html) allows the user to login if they already have a registered username. If the username is not recognised, the user is asked to register to play the game.
1. On both the log in and the register page, a user who is successfully registered or logged in is redirected to the riddles page. Their name and current score will appear in the header (see [base template](templates/base.html)) A shuffled riddle list is prepared at this time by reading the content of the [riddles file](data/riddles.json) into a session-specific variable.
1. The [riddles page](templates/riddle.html) loads the shuffled riddle list into the jinja template where the riddle and answer are inserted: the riddle where the user can see it, the answer in a hidden form field for comparing to the answer inputted by the user, making sure the required answer matches the question.
1. When a user answers a riddle, they're redirected to the [answer page](templates/answer.html) where they are told whether it was correct or not and what the expected keyword was. They're also shown how far they are in the game (X questions left) and the click of a button will redirect them to the next question or, if they've reached the last question, write their score to the [leaderboard file](data/scores.json) and redirect them to the [leaderboard page](templates/leaderboard.html).
1. This same leaderboard page can also be accessed by clicking the View Leaderboard navigation item (see [base template](templates/base.html)).
1. When the user clicks the log-out button in the nav bar, their session will be discarded and a [Logged Out page](templates/loggedout.html) will appear to confirm they logged out and to thank them for playing.



