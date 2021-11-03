from flask import Flask, render_template
from mock_eq import app

@app.route("/")
@app.route("/mock-eq", methods=['GET'])
def mock_eq():
    return render_template('base.html', title='Base Page')
