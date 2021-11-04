from flask import Flask, render_template, redirect
from mock_eq import app

@app.route("/")
@app.route("/mock-eq", methods=['GET'])
def mock_eq():
    # set eQ to INPROGRESS
    return render_template('base.html', title='Base Page')

@app.route("/receipt")
def receipt():
    # set up pubsub receipt
    # set eQ to COMPLETE
    return redirect("http://localhost:8082")
