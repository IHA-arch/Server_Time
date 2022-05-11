from flask import Flask,request
from datetime import datetime
import json
app=Flask(__name__)

@app.route("",methods=['GET','POST'])

def handle_request():
    if request.method=='POST':
        return "rrr"
    if request.method=='GET':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data_set={'TIME':current_time}
        json_dump=json.dumps(data_set)
        return json_dump
