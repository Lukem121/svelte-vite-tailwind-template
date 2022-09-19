import os
import openai
from flask import Flask, render_template

#create a flask app / a file that is app that serves your website
app = Flask(__name__)
openai.api_key = 


#base url
@app.route('/', methods = ("GET", "POST"))
#home page
def home():
    #return render_template('home.html')
    if request.method == "POST": 
        animal = request.form["animal"]
        response = openai.Completion.create(
            model = "text-davinci-001",
            prompt = generate_prompt(animal),
            max_token = 6
        )
        return rediirect(url_for("home", result=response.choices[0].text))
    result = request.args.get("result")
    return render_template("home.html", result=result)

@app.route('/about')
def about(): 
    return 'This is an AI generated website'


def generate_prompt(): 
    