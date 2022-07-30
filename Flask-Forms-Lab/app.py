from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)



facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]
username = "ahmad"
password = "mashe"

@app.route('/', methods = ['GET','POST'])  # '/' for the default page
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        if request.form["username"] == username and request.form["password"] == password:
        	return render_template("home.html",facefriends = facebook_friends)
            
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/friends_exists/<string:friendusername1>',methods = ['GET','POST'])
def frienduser (friendusername1):
    if (friendusername1 in facebook_friends):
    	return render_template("friend_exists.html",hey= "true")
    else:
        return render_template("friend_exists.html",hey= "false")
if __name__ == "__main__":  # Makes sure this is the main process
    app.run( # Starts the site
    debug=True
    )
