from flask import render_template, flash, redirect, url_for, abort
from app import app
from app.forms import LoginForm, RegistrationForm, MakePostForm, ReplyForm, updateBioForm, emailForm, BlessCurseForm
from flask_login import current_user, login_user
from flask_login import logout_user
from app.models import User, Post, Reply, Post_BC
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db


@app.route('/', methods=['GET', 'POST'])
@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    form = MakePostForm()
    allUsers = User.query.all()
    if form.validate_on_submit():
        post = Post(title=form.title.data, desc=form.desc.data,
                    user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return render_template('homepage.html', title='Home', posts=Post.query.filter().order_by(Post.blesses), form=form, user=allUsers)
    return render_template('homepage.html', title='Home', posts=Post.query.filter().order_by(Post.blesses), form=form, user=allUsers)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/delPost/<postid>', methods=['GET', 'POST'])
def delPost(postid):
    myPost = Post.query.get(postid)
    db.session.delete(myPost)
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/delUser/<userid>', methods=['GET', 'POST'])
def delUser(userid):
    myUser = User.query.get(userid)
    db.session.delete(myUser)
    db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/delReply/<replyid>', methods=['GET', 'POST'])
def delReply(replyid):
    myReply = Reply.query.get(replyid)
    db.session.delete(myReply)
    db.session.commit()
    return redirect(url_for('homepage'))


@app.route('/tutorial')
def tutorial():
    return render_template('tutorialpage.html', title='Tutorial')


@app.route('/topicpage/<postid>', methods=['GET', 'POST'])
def topic(postid):
    allUsers = User.query.all()
    myPost = Post.query.get(postid)

    if myPost is None:
        return render_template('404.html'), 404

    rForm = ReplyForm()
    bcForm = BlessCurseForm()

    if rForm.rSubmit.data and rForm.validate():
        reply = Reply(post_id=postid, text=rForm.text.data,
                      stance=('True' == rForm.stance.data), user_id=current_user.id)
        db.session.add(reply)
        db.session.commit()
        myReply = Post.query.get(postid).p_replies.all()
        return render_template('topicpage.html', title='Topic', post=myPost, 
                               replies=myReply, form=rForm, bcForm=bcForm, user=allUsers)

    if bcForm.bcSubmit.data and bcForm.validate():
        blessed = ('bless' == bcForm.choice.data)
        thePost = myPost
        post_bc_query = thePost.user_votes.filter_by(user_id=current_user.id).first()
        if  post_bc_query == None: 
            post_bc = Post_BC(post_id=thePost.id, user_id=current_user.id, stance=blessed)
            if blessed == True:
                thePost.blesses = thePost.blesses + 1 
            else:
                thePost.curses = thePost.curses + 1
            db.session.add(post_bc)
            db.session.commit()
        elif post_bc_query.stance != blessed: 
            if blessed == True:
                thePost.blesses +=  1 
                thePost.curses -=  1
            else:
                thePost.curses +=  1
                thePost.blesses -=  1 
            post_bc_query.stance = blessed
            db.session.commit()

        myReply = myPost.p_replies.all()
        return render_template('topicpage.html', title='Topic', post=myPost, 
                               replies=myReply, form=rForm, bcForm=bcForm, user=allUsers)
        
    myReply = myPost.p_replies.all()
    return render_template('topicpage.html', title='Topic', post=myPost, 
                               replies=myReply, form=rForm, bcForm=bcForm, user=allUsers)


@app.route('/bc/<int:reply_id>/<option>')
@login_required
def applyBCtoReply(reply_id, option):
    if option == 'bless':
        current_user.blessReply(reply_id=reply_id)
    elif option == 'curse':
        current_user.curseReply(reply_id=reply_id)
    db.session.commit()
    return redirect(request.referrer)
        


@app.route('/profile/<userid>')
def profile(userid):
    allPost= Post.query.all()
    myUser = User.query.get(userid)
    if myUser == None:
        return redirect(url_for('homepage'))
    return render_template('profile.html', title='Profile', user=myUser, post=allPost)


@app.route('/ubc/<int:user_id>/<option>')
@login_required
def applyBCtoUser(user_id, option):
    if option == 'bless':
        current_user.blessUser(user_id=user_id)
    elif option == 'curse':
        current_user.curseUser(user_id=user_id)
    db.session.commit()
    return redirect(request.referrer)


@app.route('/updateBio/<userid>', methods=['GET', 'POST'])
def updateBio(userid):
    myUser = User.query.get(userid)
    form = updateBioForm()
    if form.validate_on_submit():
        myUser.bio = form.newBio.data
        db.session.commit()
        return render_template('profile.html', title='Profile', user=myUser)
    return render_template('changeBio.html', title='Change Bio', user=myUser, form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = emailForm()
    if form.validate_on_submit():
        flash('Email Sent to the administration team')
        return render_template('contact.html', title='Contact', form=form)
    return render_template('contact.html', title='Contact', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('homepage')
        return redirect(next_page)
    return render_template('signin.html', title='Sign In', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.admin = False  # user not admin by default
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('signin'))
    return render_template('signup.html', title='Sign Up', form=form)
