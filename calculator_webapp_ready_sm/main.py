from src.calculator import Calculator
from flask import Flask, render_template, request


cal = Calculator()
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # Default values
    default_num1 = 50
    default_num2 = 80
    
    #Initialize variables
    result = ""
    num1 = default_num1
    num2 = default_num2
    operator = ""

    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operator = request.form["operator"]

        try:
            if operator == "+":
                result = cal.add(float(num1), float(num2))
            elif operator == "-":
                result = cal.substract(float(num1), float(num2))
            elif operator == "*":
                result = cal.multiply(float(num1), float(num2))
            elif operator == "/":
                result = cal.divide(float(num1), float(num2))
            else:
                result = "Invalid operator"
        except Exception as e:
            result = str(e)

    return render_template("index.html", result=result, num1=num1, num2=num2, operator=operator)


@app.route("/Magu")
def health():
    return "Designed for Magu"


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
