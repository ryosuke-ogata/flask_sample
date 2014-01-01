# -*- coding: utf-8 -*-
import os, logging
from werkzeug.utils import secure_filename
from flask import request, Blueprint, render_template, redirect, url_for

app = Blueprint('upload', __name__, url_prefix='/upload')

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt'])

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('upload/index.html')

@app.route('/submit', methods=['POST'])
def submit():
    error = u'エラーが発生しました。'
    if request.method == 'POST':
        f = request.files['the_file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(UPLOAD_FOLDER, filename))
            # ファイル保存後に結果画面へリダイレクト
            return redirect(url_for('.result') + "?filename=%s" % filename)
        elif f is None:
            error = u'ファイルが受信できません。'
        else:
            error = u'このファイルはアップロードできません。[filename=%s]' % f.filename
    return render_template('upload/index.html', error=error)

@app.route('/result', methods=['GET'])
def result():
    filename = request.args.get('filename', '')
    if filename is not None and filename != '':
        return render_template('upload/result.html', filename=filename)
    return render_template('upload/index.html', error=u'リクエストが不正です。')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS