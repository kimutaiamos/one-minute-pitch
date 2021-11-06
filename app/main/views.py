from flask import render_template,redirect,url_for
from wtforms.i18n import messages_path
from .import main
from..import db,photos
from..models import pitches,User,Comments
from.forms import PitchForm,CommentForm,Updateprofile
from flask_login import login_required,current_user



#views
@main.route('/')
def index():
    
    message= 'Hey'
    title='Pitch it up'
    return render_template('index.html',message=message,title=title)

@main.route('/pitch',methods= ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm