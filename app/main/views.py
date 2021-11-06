from flask import render_template,redirect,url_for
from werkzeug.exceptions import abort
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

    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        comment = form.comment.data

        new_pitch = pitches(title = title,category =category,pitch = pitch,user_id=current_user_id)
        title = 'New pitch'
        new_pitch.save_pitch()

        return redirect(url_for('main.index'))
    return render_template('pitch.html',pitch_entry = form)

@main.route('/user/<uname>')
def category(cate):
     '''
     returns pitches byt category
     '''
     category = pitches.get_pitches(cate)
     title = f'{cate}'
     return render_template('categories.html',title = title, category = category)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


    
