from flask import Flask, request, jsonify
from db.models import *
app = Flask(__name__)

Integer_db = Integersdb()

@app.post('/integer')
def post_integer():
    body = request.get_json()
    curr_value = int(body['integer'])
    prev_val = list(Integer_db.get_integer())
    
    if len(prev_val) == 0:
        Integer_db.post_integer(curr_value) 
        return jsonify({"value": curr_value})
    
    else:
        prev_val_id = prev_val[0]["_id"]
        Integer_db.replace_integer(prev_val_id, curr_value)     
        return jsonify({"value": curr_value})

@app.get('/')
def get_integer():
    item = list(Integer_db.get_integer())

    return jsonify({"value": item[0]["value"]})


if __name__=="__main__":
    app.run(debug=True)