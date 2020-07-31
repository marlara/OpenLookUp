from flask import Blueprint, render_template, abort

search = Blueprint('search', __name__, template_folder='templates')

@search.route('/search')
def show():
    return render_template('base.html')