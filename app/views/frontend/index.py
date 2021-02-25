from flask import render_template
from . import frontend
from app import db
from app.models.user import User


@frontend.route('/', methods=['GET', 'POST'])
def index():

    return render_template('frontend/index.html', title="I am frontend")
