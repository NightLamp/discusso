# discusso

# Purpose

The purpose of discusso is to provide a platform for people to rate and dicuss user generated content in the form of opinions. Users submit their opinion on a subject and get 'blessed' or 'cursed', referring to whether other users agree or disagree respectively. Each opinion can also be replied to by other users, who state whether their response is in agreement or disagreement with the post. What separates discusso from other website of this nature is that score of each reply to a post influences the score of the post. Lets walk through some examples:

Bruce really likes dogs, but hates cats. He decides to use discusso to voice this opinion, and gets 10 blesses and 5 curses in the first hour. Another user, Sherry, decides that she doesn't agree with Bruce, as she prefers cats more than dogs. She curses him which raises Bruce's posts curses to 6. Furthermore Sherry decides to voice her opinion on why cats are better than dogs. She responds to Bruces post with a reply in the comment section. Sherrys post gets 5 blesses and 3 curses. As Sherry has stated that this reply is in disagreement with the post, this causes the posts blesses value to increase by the amount of curses Sherrys reply has, and curses to increase by the amount of blesses Sherrys post has. If Sherrys post had of been in agreement with Bruces, the blesses of the post would increase by the amount of blesses this reply has, and the curses would increase by the amount of curses the reply has. 

The overall votes of a post determines how the post was viewed by the community. A post with high blesses and low curses, is a post that is generally agreed with by the community. A vote with the opposite, would be generally disagreed with by the community. A controversial post, would be a post whether the difference in the blesses and curses is small, with respect to have many people have voted on it. Each user can also be voted on by other users, as a reflection as how they are viewed by their community.

# Architecture

The website is designed to revolve around the homepage. The homepage is the first page you see when you enter the website and is a list of the most recent topics posted by users of the website, with the newest bubbling to the top. From here, you can view each individual post, to see the replies to the post and scores accumulated by the post. 

Each post is associated with a user. From either the homepage, or an individual topic page, the user can navigate to the writer of a post or reply. This will navigate to the users profile page. The profile page contains a picture of the user, a small blurb about themselves written by the user, and a list of all the recent posts by that user. 

Anybody can view profiles and posts on discusso. In order to vote, reply or create a new topic, you must first be a user. A button to sign in is available from the topbar, and if you are not already registered, this links to a form for you to become registered. Once registered you have free reign to create posts and replies, and also have the ability to delete and post that you have created. 

If at any point there is confusion on the webpage, the webpage has two options. The first is the tutorial page which takes you step by step through using the webpage, and the second is the ability to contact administration. The contact details are provided for the administration team in the contact section, but another available option is to anonymously email the team from the built in email sender. This allows users to report issues and concerns anonymously. 

The website is run by administator accounts. Administrator account are regular accounts that have been given this attribute through the backend. These accounts have all the ability of regular accounts, but have the ability to remove any user, post or reply as they see fit. They have total control over the site. 

# How to launch discusso

To launch discusso a virtual environment encorporating everything in requirements.txt is required. Once this is established fork the repository into this environment and run 'Flask'. This will allow the website to be used on localhost.

Discusso is designed for linux and relies on Flask. It is reccommended that venv is used to create a virtual environment for discusso. Doing so allows discusso to run on same version of packages at the time of development - resulting in no portability issues. 

To make a virtual environment run the following command in the project root directory.
`$ python -m venv venv'

To activate the virtual environment, run:
`$ venv/bin/activate`

And finally, to install all packages run the command:
`$ pip install -r requirement.txt`

You now have all the required packages ready. To run discusso, use the following command:
`flask run`

You can now access discusso with a web browser at the address localhost:5000

To use an administrative account, a prebuilt account with the username: admin, and the password: admin, has been created. Alternatively, you can create or use any account (all sample accounts have their password the same as their username) and change the account privledges through the backend through flask shell:

Run:
`flask shell`

Find the users userid, easiest way is through the all query:
`User.query.all()`

Use the userid the find the specific user instance, and change its admin field to true:
`User.query.get(<userid>).admin = True`

Commit the changes to the database:
`db.session.commit()`

You have now created a administrative user.


# Unit Testing

We were not able to encorporate any unit testing into discusso. Although throughout every commit we have been testing each aspect of the project; adding users, deleting users, creating posts, deleting posts e.t.c., we could not configure a testing environment in flask to automate this process. 

# References:
Praying hand image: http://clipart-library.com/clipart/516920.htm
pentagram image: http://clipart-library.com/clipart/527990.htm
jQuery validation guide: http://form.guide/jquery/validation-using-jquery-examples.html
Flask-Mega Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Most information was sourced from lecture slides and tutorials.