from flask import Flask, render_template, redirect, request
from mock_eq import app

@app.route("/")
@app.route("/session", methods=['GET'])
def mock_eq():
    token = request.args.get('token', None)
    return render_template('base.html', title='Mock eQ')

@app.route("/receipt")
def receipt():
    # set up pubsub receipt
    # set eQ to COMPLETE
    return redirect("http://localhost:8082/surveys/todo")
