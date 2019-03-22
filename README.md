# CITS3403
CIT4303 unit assignment, making a website with some form of social voting system

The application should perform some kind of voting or ranking activity (social choice), based on the inputs from users.
The application should be written using HTML, CSS, Flask, AJAX, JQuery, and Bootstrap. 
Must be a multi user web application.

# Ideas

* Music/Movie Polls
* Ranking recipes
* Ranking the best fishing/surfing spots in Perth
* Find the best units at UWA.
* People rater (if you want to go really bad link it to fb or other social media)
* Best uni clubs
* Best laptops/phones/devices
* A betting website
* Best parking spots for uni
* Argument solver

# Final Decision

* Argument solver

# Concept 

This website provides a platform for users to express their opinions on base arguments and recieve other user responses.

To do this, the website implements a voting system that allows for people to vote on a base argument with a simple "agree" 
or "disagree" anonomously, or optionally, when signed in, provide an reasoning argument for their vote that can be discussed 
by other users with debuttle arguments. 


# Potential Voting Algorithm 

The weight of a vote will be determined by the "popularity" of its linked reasoning argument and the "popularity" of its 
debuttle arguments.

The base argument will start at a score of 0. Users can then vote anonomously without a reasoning arg with a weight of 1(?).
Users can also link a reasoning arg to their vote, which can itself be voted on. if the reasoning arg gets more "agree"
votes than "disagree", then its weight will increase from 1 proportionatly to to the ratio of agree to disagree and the overall
agree votes it recieves. A reasoning vote can only ever hit a minimum of 0. Furthermore, a reasoning arg can also receive a debuttle
arguement which is an argument based vote which users can vote on. This can also not go further below 0 votes.

# Website Page Layout

The website will require a 'Discusssion Board' page, a 'Tutorial' page, a 'User Profile' page, a 'sign in/sign' up page, a 'Contact/Report' page and a 'Topic' page 
for every base argument.

Discussion Board:
The discussion Board will be a list of topics or 'base arguments' submitted by the users. [The topics will be listed chronologically?] and
will detail the argument raised, the user raising it, and the current vote [vote percentage?] for the topic.

Tutorial Page:
This page will be a simplistic page detailing to users what the website is about, and will explain how to use the website.

User Profile:
This page is to describe an inidividual user. It will feature an user profile (an 'about me'), a user picture, the number of followers a user has,
and the option to follow the user, and the top argument and top comment the user has left on the website.

Sign up/sign in:
This page will be a simple page to allow users to sign into their profile and or sign up if they do not already have a user account.

Contact/Report:
This page will provide users with contact details of the administrator, and will provide the user with the ability to report other users for
breaking website guidelines.

Topic:
The topic page will be a detailed version of a users base argument. Here the score of the argument will be shown, as well as statistic measures
for the argument. This page will also show reasoning arguments, their votes, and debuttle arguments to each reasoning argument, which
also shows their vote.
  

