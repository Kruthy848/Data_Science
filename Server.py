from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello! Flask server is working perfectly"


@app.route('/get_Category',methods=['GET'])
def get_Category():
    response = jsonify({
        'Category' : util.get_Category()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_sales_revenue', methods = ['POST'])
def predict_sales_revenue():
    Category = request.form['Category']
    Income = float(request.form['Income'])
    Price = float(request.form['Price'])
    Discount_Percent = int(request.form['Discount_Percent'])
    Units_Sold = int(request.form['Units_Sold'])
    Cost = float(request.form['Cost'])
    response = jsonify({
        'estimated_revenue' : util.get_predict_revenue(Category,Income,Price,Discount_Percent,Units_Sold,Cost)
    }) 
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask server for Predicting Revenue")
    util.load_saved_artifacts()  
    app.run()