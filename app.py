#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, redirect, jsonify
from werkzeug.utils import secure_filename
import numpy as np
import json
import os
import subprocess
import re
import shutil
import sys

try : 
	reload(sys)  
	sys.setdefaultencoding('utf8')  
except :
	pass
	
PNS = 'data/pns.txt'

app = Flask(__name__)
app.config['PNS'] = PNS


@app.route('/txt2pn', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        text = request.json['text']
        pns = set(line.strip() for line in open(app.config['PNS']))
        text = re.sub("[a-z\\/,\.;:!\%\$*\?\+_()\[@\{\}\]#'\^]", '',
                      str(text)).split()
        text = [word for word in text if len(word) > 5
                and any(char.isdigit() for char in word)]
        (nope, yup) = ([], [])
        for b in text:
            if b in pns:
                yup.append(b)
        (pn, c) = np.unique(yup, return_counts=True)
        res = {}
        for i in range(len(pn)):
            res[pn[i]] = c[i]
        res = re.sub('"', '', str(res))
        res = re.sub("'", '"', res)
        return jsonify(res)
    return 'Welcome to txt2pn WS'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)