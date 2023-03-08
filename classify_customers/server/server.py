from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/dummy',methods=['GET'])
def dummy():
    response=jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict',methods=['GET','POST'])
def predict():
    a1 = int(request.form['Gender'])
    a2 = int(request.form['Ever_Married'])
    a3 = int(request.form['Age'])
    a4 = int(request.form['Graduated'])
    a5 = int(request.form['Profession'])
    a6 = float(request.form['Work_Experience'])
    a7 = int(request.form['Spending_Score'])
    a8 = float(request.form['Family_Size'])
    a9 = int(request.form['Var_1'])
    print(a1, a2, a3, a4, a5, a6, a7, a8, a9)
    response=jsonify({
        'prediction':util.estimation(a1, a2, a3, a4, a5, a6, a7, a8, a9)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    util.load_saved_artifacts()
    app.debug=True
    app.run()