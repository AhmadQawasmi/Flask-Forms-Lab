from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "ahmad"
password = "mashe"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods = ['get','post'])  # '/' for the default page
def login():
	if request.method =='get':

return render_template('login.html')
  else:
   if username ==	request.form["username"] == username and request.form["password"] == password:        
  	       return redirect(url_for('home'))
  	else
  	return redirect(url_for('login'))
@app.route('/home')
def home():
	return render_template("home.html")
@app.route('/real_friends/<string:friendusername1>',methods = ['get','post'])
def frienduser (friendusername1):
	if (friendusername1	in facebook_friends);
	return render_template("real_friends.html",hey= "true")
	else:
		return render_template("real_friends.html",hey= "false")
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)