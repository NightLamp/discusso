from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    
class MakePostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    desc = StringField('Description')
    submit = SubmitField('Post It')



class ReplyForm(FlaskForm):
    text = StringField('reply', validators=[DataRequired()])
    stance = RadioField('stance', choices=[('True','for'),('False','against')])
    rSubmit = SubmitField('Post It')

class BlessCurseForm(FlaskForm):
    thePost = None
    choice = RadioField('your vote', choices=[('bless','bless'),('curse','curse')])
    bcSubmit = SubmitField('vote')
     
    def setThePost(thePost):
        this.thePost = thePost
        return;
