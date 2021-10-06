from flask import Flask, redirect, url_for, request,render_template
import json

from TwitterAPI import retrieve_tweets
app = Flask(__name__)


@app.route('/')
def home_screen():
   return render_template("index.html")


@app.route('/Tweets',methods = ['POST', 'GET'])
def fetch_tweets():
   if request.method == 'POST':
      search_term = request.form['search-term']

      jsonStr = retrieve_tweets(search_term)

      return render_template("index.html",tweets = jsonStr)
   else:
      pass




if __name__ == '__main__':
   app.run(debug = True)

