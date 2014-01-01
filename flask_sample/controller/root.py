# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
app = Blueprint('root', __name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('root/index.html')
