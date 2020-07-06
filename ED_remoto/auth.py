"""Routes for user authentication."""
from flask import redirect, render_template, flash, Blueprint, request, url_for

from .forms import LoginForm, SignupForm
from .models import db, User

# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')



@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():


    return render_template('signup.jinja2',
                           title='Create an Account.',
                           form=signup_form,
                           template='signup-page',
                           body="Sign up for a user account.")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.jinja2',
                           form=login_form,
                           title='Log in.',
                           template='login-page',
                           body="Log in with your User account.")

