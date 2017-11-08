from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__) #create Flask object

@app.route("/") #assign following fxn to run in response to root route request
def hello_world():
    return "No hablo queso!"

if __name__ == "__main__": #do not run if this file is imported as module
    app.run()
