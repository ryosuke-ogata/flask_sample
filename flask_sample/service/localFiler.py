# -*- coding: utf-8 -*-
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt'])

def saveTxtFile(f):
    # 呼び出し側でわけわからなくなるので、最初に型定義しておきたい
    # 複雑条件の場合には、コメントも
    ret = {
           'result': 'failure',
           'error': None,
           'filename': None,
           'filepath': None,
           }
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        ret.filename = filename
        ret.filepath = os.path.join(UPLOAD_FOLDER, filename)
        f.save(ret.filepath)
        ret.result = 'success'
        return ret
    elif f is None:
        ret.error = u'ファイルが受信できません。'
    else:
        ret.error = u'このファイルはアップロードできません。[filename=%s]' % f.filename
    return ret

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
