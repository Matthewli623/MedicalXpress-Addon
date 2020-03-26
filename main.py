from flask import Flask, jsonify
import json
import getdata
from OpenSSL import SSL

app = Flask(__name__)

mydata = [{
    'name': 'Eltirst store',
    'items': [{'name': 'my item 1', 'price': 30}],
},
    {
    'name': 'Eltonsecond store',
    'items': [{'name': 'my item 2', 'price': 15}],
},
]
# 只接受POST方法访问
@app.route("/getdata")
def check():
    # 默认返回内容
    return_dict = {'statusCode': '200',
                   'message': 'successful!', 'result': False}
    # 判断入参是否为空
    response = app.response_class(
        response=mydata,
        mimetype='application/json'
    )
    return response


@app.route('/')
def index():
    return "Hello World"


if __name__ == "__main__":
    mydata = getdata.getsjson()
    app.run(debug=True, host='0.0.0.0')
