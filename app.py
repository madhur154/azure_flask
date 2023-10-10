from flask import Flask  

app = Flask(__name__)

@app.route('/')   
def hello_world():  
    return "hello, this is our ci/cd demo for python app";  

if __name__ =='__main__':  
    app.run(debug = True, host='0.0.0.0')
