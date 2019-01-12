# encoding:utf-8


import os
import random
import time
import json

from flask import Flask, request, send_file, redirect, render_template_string
from flask import render_template

app = Flask(__name__)

dirpath = os.path.dirname(os.path.abspath(__file__))


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        files = request.files
        if len(files) < 2:
            return '请完整上传两个文件'

        # generate distinc number
        distinc = '{random_num:0>3}:{time_stamp}'.format(random_num=random.randint(0, 999),
                                                         time_stamp=str(int(time.time())))

        # base path
        base_path = os.path.join(os.path.dirname(__file__), 'TestData')

        # fetch files
        for i in files:
            f = files[i]
            f_name = os.path.splitext(f.filename)
            name, suffix = f_name[0], f_name[1]
            print(suffix)
            if suffix != '.jpg' and suffix != '.jpeg':
                return '不好意思现在还不支持{suffix}文件，only Jpg'.format(suffix=suffix)

            f.save('{base_path}/{distinc}_{type}.jpg'.format(base_path=base_path, distinc=distinc, type=i))

        return distinc


@app.route('/snipaste', methods=['GET'])
def snipaste():
    print('正在裁剪衣领标中的logo')


@app.route('/classify', methods=['GET', 'POST'])
def classfy():
    if request.method == 'POST':
        data = eval(request.data)
        print('成功接收识别码 =======>', data)
        distinc = data.get('distinc', '')

        # snipaste

        # classify logo

        # classify main


        return '200'


if __name__ == '__main__':
    print('Flask 正在启动.........')

    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port, debug=True)

    print('Flask 启动完成.........')
