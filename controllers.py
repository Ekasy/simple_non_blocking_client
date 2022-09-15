from flask import Blueprint
from flask import render_template, jsonify


viewer = Blueprint('viewer', __name__)


LIKE_STATUS = 1


@viewer.route('/')
def root():
    return {
        'status': 'ok',
    }


@viewer.route('/page')
def base_page():
    return render_template('template.html')


@viewer.route('/check_status')
def check_status():
    global LIKE_STATUS
    if LIKE_STATUS % 5 != 0:
        status_msg = 'not_ready'
        LIKE_STATUS += 1
    else:
        status_msg = 'ready'
        LIKE_STATUS = 1

    ans = jsonify({'status': status_msg})
    ans.status_code = 200
    return ans
