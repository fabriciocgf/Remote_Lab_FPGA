from flask import Blueprint, render_template, Response, request, jsonify
from flask import current_app as app
from werkzeug.utils import secure_filename
import os

# Set up a Blueprint
main_bp = Blueprint('main_bp', __name__,
                     template_folder='templates',
                     static_folder='static')

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/Controle')
def Controle():
    return render_template('Controle.html')

@main_bp.route('/Upload')
def Upload():
    return render_template('Upload.html')

@main_bp.route('/Arquivo', methods=['GET', 'POST'])
def Arquivo():
    if request.method == 'POST':
        file = request.files['inputptbr[]']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify(file.filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

