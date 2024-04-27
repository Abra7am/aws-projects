from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username

def find_emails(keyword):
    user_emails = User.query.filter(User.username.like(f'%{keyword}%')).all()
    return [(user.username, user.email) for user in user_emails]

def insert_email(name, email):
    if not name or not email:
        return 'Username or email can not be empty!!'
    existing_user = User.query.filter_by(username=name).first()
    if existing_user:
        return f"User {name} already exists"
    new_user = User(username=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"User {name} and {email} have been added successfully"

@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':
        user_keyword = request.form['user_keyword']
        user_emails = find_emails(user_keyword)
        return render_template('emails.html', name_emails=user_emails, keyword=user_keyword, show_result=True)
    else:
        return render_template('emails.html', show_result=False)

@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        username = request.form['username']
        useremail = request.form['useremail']
        result = insert_email(username, useremail)
        return render_template('add-email.html', result_html=result, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
