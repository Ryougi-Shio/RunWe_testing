# 运行此函数以搭建后端，提供api。
# ==================================
from flask import Flask, jsonify, abort, request, make_response, url_for, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from integration_testing.ArticleTest import doA
from integration_testing.ManagerTest import DoM
from integration_testing.FollowTest import doF
from integration_testing.UserTest import DoU



# =================================
app = Flask(__name__, template_folder='', static_folder='')
CORS(app, resources=r'/*')  # 注册CORS, "/*" 允许访问所有api
auth = HTTPBasicAuth()
# ================================================#
#                 以下是对API的定义               #
# ================================================#
"""
（待改进）
完成图像上传->预测->保存图片。
流程：
1. 规定api名称，前端调用后，上传图片，图片放到 ./uploads里
2. 然后调用predict函数，从/uploads里读取图片，预测，然后把结果图片保存到.atic/label
3. 然后前端获取文件名，从label/文件名 拿图
"""


@app.route('/do', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    if request.method == 'POST' or request.method == 'GET':
        print(request.form)
        load= request.form.get("test")

        if load=="article":
            pass
        elif load=="follow":
            doF();
        elif load=="user":
            DoU();
        elif load=="manager":
            DoM()
        else:
            return "False"

    return "True"
# ==============================================================================================================================
#                                                                                                                              
#                                           Main function                                                        	            #						     									       
#  				                                                                                                
# ==============================================================================================================================
@app.route("/")
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

