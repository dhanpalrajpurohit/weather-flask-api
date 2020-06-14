from flask import Flask, request, render_template
import requests
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def checkNews():
    url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
    data = requests.get(url).json()
    newsDatas = data["articles"]
    return render_template("checkNews.html",newsDatas=newsDatas)

if __name__ == '__main__':
    app.run(debug=True)
