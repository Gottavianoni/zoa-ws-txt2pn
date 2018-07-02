#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename
import json
import os
import subprocess
import re
import shutil

UPLOAD_FOLDER = 'uploads/'
TIKA_EXE = 'external/'
TIKA_INPT = 'uploads/'
FULL = os.getcwd()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TIKA_EXE'] = TIKA_EXE
app.config['TIKA_INPT'] = TIKA_INPT
app.config['FULL'] = FULL


@app.route('/pdf2txt', methods=['GET', 'POST'])
def contact():
svr='dhchvie0.eu.airbus.corp'
svr='44.55.118.40'
prt=34615
usr='MAT**SCU_M'
pwd='D*ni*rs'
global conn
conn=pyhdb.connect(svr,prt,usr,pwd)
 
cursor=conn.cursor()
 
text = re.sub("[a-z\\/,\.;:!\%\$*\?\+_()\[@\{\}\]#'\^]", '', text).split()
text = [word for word in text if len(word)>5 and any(char.isdigit() for char in word)]
 
for b in text:
            cursor.execute("""select m.mfrpn,m.mtart,zzadt,zzaibo from "SLT_PHC_PCS_DHC".mara as m where m.mfrpn='"""+b+"';")
            ret=cursor.fetchone()
            if not ret:
                        nope.append(b)
            else:
                        yup.append(b)
pn,c = np.unique(yup, return_counts = True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5001)
