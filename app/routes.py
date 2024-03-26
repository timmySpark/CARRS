from flask import render_template
from app import app, db
from .models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

