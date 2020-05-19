from flask import Flask, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def index():
    print("----------------------")
    print("index called")
    print("----------------------")
    return render_template('index.html')

@app.route("/ml")
def ml():
    print("----------------------")
    print("ML called")
    print("----------------------")
    return render_template('ML.html')

@app.route("/unemployment")
def unemployment():
    print("----------------------")
    print("unemployment called")
    print("----------------------")
    return render_template('unemployment.html')

@app.route("/other-data")
def otherdata():
    print("----------------------")
    print("other-data called")
    print("----------------------")
    return render_template('other_data.html')

if __name__ == '__main__':
    app.run(debug=True)