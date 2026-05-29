from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route("/")
def index():
    return "Flask aaaaa"
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)