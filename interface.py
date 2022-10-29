from flask import Flask, jsonify, render_template, request
from Project_app.utils import Iris
import config

app = Flask(__name__)

######################################### Base API #############################################################
@app.route("/")
def base():
    print("This is base api")
    return "Welcome to Flask"

######################################### class predicion API ##################################################
# @app.route("/classpredicion")
# def get_class():
#     SepalLengthCm	= 6.2
#     SepalWidthCm = 1.4
#     PetalLengthCm = 0.2
#     PetalWidthCm = 0.4

#     get_iris = Iris( SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
#     class1 = get_iris.get_predicted_class()[0]

#     return f"The Predicted class is {class1}"


######################################### Home API #############################################################

@app.route("/home")
def home():
    print("This is home API")
    return render_template('index.html')


######################################### class predicion API #############################################################
# @app.route("/classpredicion_html", methods=['GET'])
# def classpredicion_htm():
#     try:
#         SepalLengthCm = request.args.get('SepalLengthCm')
#         SepalWidthCm = request.args.get('SepalWidthCm')
#         PetalLengthCm = request.args.get('PetalLengthCm')
#         PetalWidthCm = request.args.get('PetalWidthCm')

#         get_iris = Iris( SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
#         class1 = get_iris.get_predicted_class()[0]

#         return render_template('output.html')
#     except:
#         return 'Error'

@app.route("/submit", methods = ["POST", "GET"])
def submit():
    if request.method == "POST":
        SepalLengthCm = float(request.form['SepalLengthCm'])
        SepalWidthCm = float(request.form['SepalWidthCm'])
        PetalLengthCm = float(request.form['PetalLengthCm'])
        PetalWidthCm = float(request.form['PetalWidthCm'])
    
    get_iris = Iris( SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    class1 = get_iris.get_predicted_class()[0]

    return f"The Predicted class is {class1}"






if __name__ == "__main__":
    app.run()












