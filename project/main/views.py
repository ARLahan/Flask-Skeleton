# main/views.py

from flask import render_template, Blueprint
from .. import app

# Create blueprint
main_bp = Blueprint('main', __name__, url_prefix='/',
                    static_folder='static',
                    template_folder='templates')


# main blueprint routes
@main_bp.route('/')
def home():
    return render_template('main/home.html', app_name=app.config['APP_NAME'])


@main_bp.route('/about')
def about():
    return render_template('main/about.html', app_name=app.config['APP_NAME'])
