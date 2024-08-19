#IMPORTS
from flask import Flask, render_template


app = Flask(__name__)
#APP ROUTES

@app.route('/')
def main_page():    
    return render_template('index/index.html')

    
@app.route('/secondary')
def contact_page():
    return render_template('secondary/secondary.html')



app.run(debug=True)
