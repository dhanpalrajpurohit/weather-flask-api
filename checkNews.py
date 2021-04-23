from flask import Flask, request, render_template
import requests
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def checkNews():
    url = "YOUR_API_KEY"
    data = requests.get(url).json()
    newsDatas = data["articles"]
    return render_template("checkNews.html",newsDatas=newsDatas)

if __name__ == '__main__':
    app.run(debug=True)
