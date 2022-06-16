from flask import Flask , request, jsonify

app = Flask(__name__)

tasks = [
    {
        'id' : 1,
        'contact no.' : "4740379174",
        'name' : "abcd"
    },
    {
        'id' : 2,    
        'contact no.' : "7942794749",
        'name' : "feg"
    }
    ]

@app.route("/add",methods = ["POST"])
def add_task():
    if not request.json():
        return jsonify({
            "status":"error",
            "message":"Add The Data"
        })
    task = {
        'id': tasks[-1]['id'] + 1,
        'contact no.': request.json['contact no.'],
        'name': request.json['name'],
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
@app.route("/get-data")
def show():
    return jsonify({
        "data" : tasks 
    })

if __name__=="__main__":
    app.run()
