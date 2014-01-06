# -*- coding: utf-8 -*-
from flask import request, Blueprint, render_template, redirect, url_for
app = Blueprint('upload', __name__, url_prefix='/upload')

import service.localFiler

@app.route('/', methods=['GET', 'POST'])
def index():
    from flask_sample import mongo
    return render_template('upload/index.html')

@app.route('/submit', methods=['POST'])
def submit():
    ret = service.localFiler.saveTxtFile(request.files['the_file'])
    if ret.result == 'success':
        # ファイル保存後に結果画面へリダイレクト
        return redirect(url_for('.result') + "?filename=%s" % ret.filename)
    elif ret.error is not None:
        error = ret.error
    else:
        error = u'エラーが発生しました。'
    return render_template('upload/index.html', error=error)

@app.route('/result', methods=['GET'])
def result():
    filename = request.args.get('filename', '')
    if filename is not None and filename != '':
        return render_template('upload/result.html', filename=filename)
    return render_template('upload/index.html', error=u'リクエストが不正です。')

