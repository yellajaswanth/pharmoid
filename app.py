from flask import Flask, render_template


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug=True)
